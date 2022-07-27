import torch

dict = {'https-www-ijcai-org-proceedings-2021-0575-pdf.pdf' : torch.Tensor([1, 2, 3, 4, 5, 6]),
    'https-www-ijcai-org-proceedings-2021-0577-pdf.pdf' : torch.Tensor([7, 8, 9, 10, 11, 12])}

for file, value in dict.items():
    #final_tensor = torch.stack(dict[file])
    print("File: ", file, "Type: ", type(dict[file]), "Shape: ", dict[file].size())

print(list(dict.values()))