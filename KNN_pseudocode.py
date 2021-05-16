
correct = 0
total_predicted_positives = 0
for i, entry in enumerate(bin_dev_data): # enumerate each person in the dev set
    dists = np.linalg.norm((bin_train_data - entry), axis=1) # calculate Euclidean distances
    topk_indices = np.argsort(dists)[:k] # sort distances and return indices
    num_positives = 0
    for person_idx in topk_indices:
        if train_labels[person_idx] == ">50K":
            num_positives += 1
    if num_positives > k/2:
        predicted_label = ">50K"
        total_predicted_positives += 1
    else:
        predicted_label = "<=50K"
    if predicted_label == dev_labels[i]:
        correct += 1

error = 1 - correct / len(bin_dev_data)
positive_rate = total_predicted_positives / len(bin_dev_data)
