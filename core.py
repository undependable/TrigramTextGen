from modell import trigramModell

class Import:
    def __init__(self, file_):
        self.content = []
        with open(file=f"{file_}", mode="r", encoding="utf-8") as content:
            for i, message in enumerate(content, 1): 
                data = message.strip().split(",")

                if len(data) > 2: self.content.append(data[2])

class Export:
    def __init__(self, file_, output_filename):
        self.messages = Import(file_).content  
        with open(file=f"{output_filename}.txt", mode="w", encoding="utf-8") as output_file:
            for message in self.messages:
                try: output_file.write(f"{message}\n")

                except: pass

def hovedprogram():
    importerFilnavn = None
    outputFil = None
    
    while True:
        print("1. Import custom file\n2. Export custom file\n3. Generate random text\n4. Quit program.")
        choice = input("> ")

        if choice == "1":
            importerFilnavn = input("Input file data: ")
            Import(importerFilnavn)

        elif choice == "2":
            outputFil = input("Output file data: ")
            Export(importerFilnavn, outputFil)

        elif choice == "3":
            if outputFil is None: outputFil = input("Type an output file: ")
            print("\n", trigramModell(outputFil.replace(".txt", "")).generate(),"\n")

        elif choice == "4": return False
hovedprogram()