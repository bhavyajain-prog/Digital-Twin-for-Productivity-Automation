# src/model_training/interest_model.py
import pandas as pd
import numpy as np
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
import pickle
import os

def train_interest_model(domain_features, n_clusters=5):
    """
    Train a model to identify clusters of similar domains as interest categories
    
    Args:
        domain_features: DataFrame with domain frequency information
        n_clusters: Number of interest categories to identify
    
    Returns:
        trained model, clusters, and scaler
    """
    if domain_features.empty or len(domain_features) < n_clusters:
        print("Not enough data to train the model yet.")
        return None, None, None
    
    # Prepare features for clustering
    features = domain_features[['visit_count', 'visit_percentage']]
    
    # Scale features
    scaler = StandardScaler()
    scaled_features = scaler.fit_transform(features)
    
    # Train KMeans clustering model
    kmeans = KMeans(n_clusters=n_clusters, random_state=42)
    clusters = kmeans.fit_predict(scaled_features)
    
    # Add cluster assignments back to the domain features
    domain_features['interest_category'] = clusters
    
    # Save the model
    os.makedirs("models", exist_ok=True)
    with open("models/interest_model.pkl", "wb") as f:
        pickle.dump((kmeans, scaler), f)
    
    return kmeans, clusters, scaler

def get_interest_profile(domain_features, kmeans, scaler):
    """
    Generate a user interest profile based on the clustered domains
    
    Args:
        domain_features: DataFrame with domain information and clusters
        kmeans: Trained KMeans model
        scaler: Trained scaler
    
    Returns:
        Dictionary describing user interests
    """
    if domain_features.empty or kmeans is None:
        return {"status": "Not enough browsing data yet"}
    
    # Get the most popular domains in each cluster
    profile = {}
    for cluster_id in domain_features['interest_category'].unique():
        cluster_domains = domain_features[domain_features['interest_category'] == cluster_id]
        top_domains = cluster_domains.nlargest(3, 'visit_count')['domain'].tolist()
        total_percentage = cluster_domains['visit_percentage'].sum()
        
        profile[f"Interest Category {cluster_id+1}"] = {
            "top_domains": top_domains,
            "percentage_of_browsing": round(total_percentage, 2)
        }
    
    return profile