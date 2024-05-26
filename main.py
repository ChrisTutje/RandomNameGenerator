import random
import json
import os

class Language:
    def __init__(self, name, data):
        self.name = name
        self.data = data

    def search(self, term):
        results = {}
        for category in ['prefix', 'root', 'suffix', 'modifier']:
            if category in self.data:
                for key, value in self.data[category].items():
                    if isinstance(value, dict):
                        if term.lower() in key.lower() or term.lower() in value.get('meaning', '').lower():
                            results[key] = value.get('meaning', '')
                    else:
                        if term.lower() in key.lower() or term.lower() in value.lower():
                            results[key] = value
        return results

def load_syllables(filepath):
    with open(filepath, 'r', encoding='utf-8') as file:
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
            meaning_text = meaning['meaning'] if isinstance(meaning, dict) else meaning  
            name_parts.append(syllable)
            meaning_parts.append(meaning_text)
    
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

def search_all_languages(languages, term):
    results = {}
    for language in languages:
        search_results = language.search(term)
        if search_results:
            results[language.name] = search_results
    return results

def load_languages():
    languages = []
    language_folders = ['Elvish', 'Human']
    for lang in language_folders:
        base_filepath = f"Conlangs/{lang}/{lang}.json"
        if os.path.exists(base_filepath):
            base_data = load_syllables(base_filepath)
            languages.append(Language(lang, base_data))
            if 'subsets' in base_data:
                for subset_name, subset_filepath in base_data['subsets'].items():
                    if os.path.exists(subset_filepath):
                        subset_data = load_syllables(subset_filepath)
                        full_data = merge_syllables(base_data.copy(), subset_data)
                        languages.append(Language(f"{lang} ({subset_name})", full_data))
    return languages

if __name__ == "__main__":

    languages = load_languages()
    
    # """Search examples"""
    # print("Search results in all languages:")
    # search_term = 'beleg'
    # all_results = search_all_languages(languages, search_term)
    # for lang, results in all_results.items():
    #     print(f'\n{lang}:')
    #     for key, value in results.items():
    #         print(f'{key}: {value}')
    

    # """==Elvish=="""
    # print("\nGeneral Elvish names:")
    # for _ in range(10):
    #     name, meaning = generate_conlang_name("elvish")
    #     print(f"Generated Name: {name}")
    #     print(f"Meaning: {meaning}")
    # print("\n" + "="*40 + "\n")
    
    # """-Dark-Elvish-"""
    # print("\nGenerating names for Dark Elvish:")
    # for _ in range(1):
    #     name, meaning = generate_conlang_name("elvish", "dark-elven")
    #     print(f"Generated Name: {name}")
    #     print(f"Meaning: {meaning}")
    # print("\n" + "-"*40 + "\n")
    
    # """-Wood-Elvish-"""
    # print("Generating names for Wood Elvish:")
    # for _ in range(1):
    #     name, meaning = generate_conlang_name("elvish", "wood-elven")
    #     print(f"Generated Name: {name}")
    #     print(f"Meaning: {meaning}")
    # print("\n" + "-"*40 + "\n")
    
    # """-Sea-Elvish-"""
    # print("Generating names for Sea Elvish:")
    # for _ in range(1):
    #     name, meaning = generate_conlang_name("elvish", "sea-elven")
    #     print(f"Generated Name: {name}")
    #     print(f"Meaning: {meaning}")
    # print("\n" + "-"*40 + "\n")
    
    # """-Snow-Elvish-"""
    # print("Generating names for Snow Elvish:")
    # for _ in range(1):
    #     name, meaning = generate_conlang_name("elvish", "snow-elven")
    #     print(f"Generated Name: {name}")
    #     print(f"Meaning: {meaning}")
    # print("\n" + "-"*40 + "\n")
    
    # """-High-Elvish-"""
    # print("\nGenerating names for High Elvish:")
    # for _ in range(1):
    #     name, meaning = generate_conlang_name("elvish", "high-elven")
    #     print(f"Generated Name: {name}")
    #     print(f"Meaning: {meaning}")
    # print("\n" + "-"*40 + "\n")
        
        
    """==Human=="""
    # print("\nGeneral Human names:")
    # for _ in range(1):
    #     name, meaning = generate_conlang_name("human")
    #     print(f"Generated Name: {name}")
    #     print(f"Meaning: {meaning}")
    # print("\n" + "="*40 + "\n")
    
    # """-Archaic-"""
    # print("Generating names for Archaic Human:")
    # for _ in range(1):
    #     name, meaning = generate_conlang_name("human", "archaic")
    #     print(f"Generated Name: {name}")
    #     print(f"Meaning: {meaning}")
    # print("\n" + "-"*40 + "\n")
    
    # """-Imperial-"""
    # print("Generating names for Imperial Human:")
    # for _ in range(10):
    #     name, meaning = generate_conlang_name("human", "imperial")
    #     print(f"Generated Name: {name}")
    #     print(f"Meaning: {meaning}")
    # print("\n" + "-"*40 + "\n")
    
    # """-Nomadic-"""
    # print("Generating names for Nomadic Human:")
    # for _ in range(10):
    #     name, meaning = generate_conlang_name("human", "nomadic")
    #     print(f"Generated Name: {name}")
    #     print(f"Meaning: {meaning}")
    # print("\n" + "-"*40 + "\n")
    
    # """-Easterling-"""
    # print("Generating names for Easterling Human:")
    # for _ in range(10):
    #     name, meaning = generate_conlang_name("human", "easterling")
    #     print(f"Generated Name: {name}")
    #     print(f"Meaning: {meaning}")
    # print("\n" + "-"*40 + "\n")
    
    # """-Dunlanding-"""
    # print("Generating names for Dunlanding Human:")
    # for _ in range(10):
    #     name, meaning = generate_conlang_name("human", "dunlanding")
    #     print(f"Generated Name: {name}")
    #     print(f"Meaning: {meaning}")
    # print("\n" + "-"*40 + "\n")
    
    # """-Highlander-"""
    # print("Generating names for Highlander Human:")
    # for _ in range(10):
    #     name, meaning = generate_conlang_name("human", "highlander")
    #     print(f"Generated Name: {name}")
    #     print(f"Meaning: {meaning}")
    # print("\n" + "-"*40 + "\n")
    
    # """-Seaguard-"""
    # print("Generating names for Seaguard Human:")
    # for _ in range(10):
    #     name, meaning = generate_conlang_name("human", "seaguard")
    #     print(f"Generated Name: {name}")
    #     print(f"Meaning: {meaning}")
    # print("\n" + "-"*40 + "\n")
    
    """-Nordic-"""
    print("Generating names for Nordic Human:")
    for _ in range(10):
        name, meaning = generate_conlang_name("human", "nordic")
        print(f"Generated Name: {name}")
        print(f"Meaning: {meaning}")
    print("\n" + "-"*40 + "\n")
        
    # """-Highlander-"""
    # print("\nGenerating names for Highland Human:")
    # for _ in range(1):
    #     name, meaning = generate_conlang_name("human", "highlander")
    #     print(f"Generated Name: {name}")
    #     print(f"Meaning: {meaning}")
    # print("\n" + "-"*40 + "\n")


    # """==Hybrid Languages=="""
    # """-Half-Elven-"""
    # print("Generating names for Half-Elvish (combining Elvish and Human):")
    # hybrid_language = [("elvish", None), ("human", None)]
    # for _ in range(1):
    #     name, meaning = generate_conlang_name(hybrid_language=hybrid_language)
    #     print(f"Generated Name: {name}")
    #     print(f"Meaning: {meaning}")
    # print("\n" + "="*40 + "\n")

