atch the preprocessing applied to the original data
sample_input = [sample_input]  # Convert to a 2D array
sample_input_scaled = scaler.transform(sample_input)  # Apply the same scaler used on the training data
sample_input_pca = pca.transform(sample_input_scaled)  # Apply PCA