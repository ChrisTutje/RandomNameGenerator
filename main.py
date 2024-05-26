import random
import json
import os

def load_syllables(filepath):
    with open(filepath, 'r') as file:
        return json.load(file)

def merge_syllables(base, additional):
    for key in additional:
        if key in base:
            base[key].update(additional[key])
        else:
            base[key] = additional[key]
    return base

def generate_name(syllables, structures):
    structure = random.choice(structures)
    parts = structure.split("-")
    name_parts = []
    meaning_parts = []
    
    for part in parts:
        if part in syllables and syllables[part]:
            syllable, meaning = random.choice(list(syllables[part].items()))
            name_parts.append(syllable)
            meaning_parts.append(meaning)
    
    name = "".join(name_parts).capitalize()
    meaning = " ".join(meaning_parts)
    return name, meaning

def load_conlang(base_filepath, subset=None):
    base_syllables = load_syllables(base_filepath)
    
    if subset and 'subsets' in base_syllables and subset in base_syllables['subsets']:
        subset_filepath = base_syllables['subsets'][subset]
        subset_syllables = load_syllables(subset_filepath)
        base_syllables = merge_syllables(base_syllables, subset_syllables)
    
    return base_syllables

def load_hybrid_language(languages_subsets):
    combined_syllables = {
        "prefix": {},
        "root": {},
        "suffix": {},
        "modifier": {}
    }
    
    for language, subset in languages_subsets:
        base_filepath = f"Conlangs/{language.capitalize()}/{language.capitalize()}.json"
        syllables = load_conlang(base_filepath, subset)
        combined_syllables = merge_syllables(combined_syllables, syllables)
    
    return combined_syllables

def generate_conlang_name(language=None, subset=None, hybrid_language=None):
    if hybrid_language:
        syllables = load_hybrid_language(hybrid_language)
    else:
        base_filepath = f"Conlangs/{language.capitalize()}/{language.capitalize()}.json"
        syllables = load_conlang(base_filepath, subset=subset)
    
    # Define multiple structures for variability
    structures = [
        "prefix-root-suffix", 
        "prefix-root", 
        "root-suffix", 
        "root",
        "prefix-prefix-root",
        "root-suffix-suffix",
        "prefix-modifier-root",
        "root-modifier-suffix"
    ]
    
    # Generate and return name and meaning
    name, meaning = generate_name(syllables, structures)
    return name, meaning

if __name__ == "__main__":

    # """==Eldarin=="""
    # print("\nGeneral Elvish names:")
    # for _ in range(1):
    #     name, meaning = generate_conlang_name("elvish")
    #     print(f"Generated Name: {name}")
    #     print(f"Meaning: {meaning}")
    # print("\n" + "="*40 + "\n")
    
    # """-Avari-"""
    # print("\nGenerating names for Dark Elvish:")
    # for _ in range(1):
    #     name, meaning = generate_conlang_name("elvish", "dark-elven")
    #     print(f"Generated Name: {name}")
    #     print(f"Meaning: {meaning}")
    # print("\n" + "-"*40 + "\n")
    
    # """-Silvan-"""
    # print("Generating names for Wood Elvish:")
    # for _ in range(1):
    #     name, meaning = generate_conlang_name("elvish", "wood-elven")
    #     print(f"Generated Name: {name}")
    #     print(f"Meaning: {meaning}")
    # print("\n" + "-"*40 + "\n")
    
    # """-Telerin-"""
    # print("Generating names for Sea Elvish:")
    # for _ in range(1):
    #     name, meaning = generate_conlang_name("elvish", "sea-elven")
    #     print(f"Generated Name: {name}")
    #     print(f"Meaning: {meaning}")
    # print("\n" + "-"*40 + "\n")
    
    # """-Falmer-"""
    # print("Generating names for Snow Elvish:")
    # for _ in range(1):
    #     name, meaning = generate_conlang_name("elvish", "snow-elven")
    #     print(f"Generated Name: {name}")
    #     print(f"Meaning: {meaning}")
    # print("\n" + "-"*40 + "\n")
    
    # """-Quenya-"""
    # print("\nGenerating names for High Elvish:")
    # for _ in range(1):
    #     name, meaning = generate_conlang_name("elvish", "high-elven")
    #     print(f"Generated Name: {name}")
    #     print(f"Meaning: {meaning}")
    # print("\n" + "-"*40 + "\n")
        

    #"""==Mannish=="""
    # print("\nGeneral Human names:")
    # for _ in range(1):
    #     name, meaning = generate_conlang_name("human")
    #     print(f"Generated Name: {name}")
    #     print(f"Meaning: {meaning}")
    # print("\n" + "="*40 + "\n")
    
    #"""-Nordic-"""
    # print("Generating names for Nordic Human:")
    # for _ in range(1):
    #     name, meaning = generate_conlang_name("human", "nordic")
    #     print(f"Generated Name: {name}")
    #     print(f"Meaning: {meaning}")
    # print("\n" + "-"*40 + "\n")
        
    #"""-Highlander-"""
    # print("\nGenerating names for Highland Human:")
    # for _ in range(1):
    #     name, meaning = generate_conlang_name("human", "highlander")
    #     print(f"Generated Name: {name}")
    #     print(f"Meaning: {meaning}")
    # print("\n" + "-"*40 + "\n")


    #"""==Hybrid Languages=="""
    #"""-Half-Elven-"""
    # print("Generating names for Half-Elvish (combining Elvish and Human):")
    # hybrid_language = [("elvish", None), ("human", None)]
    # for _ in range(1):
    #     name, meaning = generate_conlang_name(hybrid_language=hybrid_language)
    #     print(f"Generated Name: {name}")
    #     print(f"Meaning: {meaning}")
    # print("\n" + "="*40 + "\n")

