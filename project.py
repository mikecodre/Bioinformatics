def dna_to_mrna():
    with open("genomic.fna", "r") as file:
        lines = file.readlines()
        var = lines[1]
        list = []
        for i in range(0, len(var), 3):
            list.append(var[i:i + 3])
        test_1 = list[0]
        temp = test_1
        temp_list = []
        for i in temp:
            temp_list.append(i)
        for i in list:
            print(
                f""" The DNA is {i} and the mRNA is {i.translate(str.maketrans({"G": "C", "C": "G", "A": "U", "T": "A"}))}""")


def dna_to_trna():
    with open("genomic.fna", "r") as file:
        lines = file.readlines()
        var = lines[1]
        list = []
        for i in range(0, len(var), 3):
            list.append(var[i:i + 3])
        test_1 = list[0]
        temp = test_1
        temp_list = []
        for i in temp:
            temp_list.append(i)
        for i in list:
            print(
                f""" The DNA is {i} and the tRNA is {i.translate(str.maketrans({"T": "U"}))}""")


def trna_to_protein():
    with open("genomic.fna", "r") as file:
        data = file.read()
        lines = file.readlines()
        # var = lines[1]
        list = []
        trnas = []
        for i in range(0, len(data), 3):
            list.append(data[i:i + 3])
        test_1 = list[0]
        temp = test_1
        temp_list = []
        for i in temp:
            temp_list.append(i)
        for i in list:
            trnas.append(i.translate(str.maketrans({"T": "U"})))
        trnas.pop(-1)
        # print(trnas)
        big_dict = {"UUU": "Phe", "UUC": "Phe", "UUA": "Leu", "UUG": "Leu", "UCU": "Ser", "UCC": "Ser", "UCA": "Ser",
                    "UCG": "Ser", "UAU": "Tyr", "UAC": "Tyr", "UGU": "Cys", "UGC": "Cys", "CUU": "Leu", "CUC": "Leu",
                    "CUA": "Leu", "CUG": "Leu", "CCU": "Pro", "CCC": "Pro", "CCA": "Pro", "CCG": "Pro", "CAU": "His",
                    "CAC": "His", "CAA": "Cln", "CAG": "Gln", "CGU": "Arg", "CGC": "Arg", "CGA": "Arg", "CGG": "Arg",
                    "AUU": "Ile", "AUC": "Ile", "AUA": "Ile", "ACU": "Thr", "ACC": "Thr", "ACA": "Thr", "ACG": "Thr",
                    "AAU": "Asn", "AAC": "Asn", "AAA": "Lys", "AAG": "Lys", "AGU": "Ser", "AGC": "Ser", "AGA": "Arg",
                    "AGG": "Arg", "GUU": "Val", "GUC": "Val", "GUA": "Val", "GUG": "Val", "GCU": "Ala", "GCC": "Ala",
                    "GCA": "Ala", "GCG": "Ala", "GAU": "Asp", "GAC": "Asp", "GAA": "Glu", "GAG": "Clu", "GGU": "Gly",
                    "GGC": "Gly", "GGA": "Gly", "GGG": "Gly", "AUG": "Met"}
        for i in trnas:
            for trna, protein in big_dict.items():
                if trna == i:
                    with open("text.txt", "a+") as test:
                        test.write(f"The tRNA is {trna} and the protein is {protein}\n")
                    # print(f"The tRNA is {trna} and the protein is {protein}")


trna_to_protein()
