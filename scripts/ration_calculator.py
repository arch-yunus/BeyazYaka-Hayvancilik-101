#!/usr/bin/env python3
"""
ration_calculator.py — THE LIVESTOCK ENCYCLOPEDIA
Precision TMR (Total Mixed Ration) Calculation & Nutritional Analysis Tool
"""

import json
import os
import argparse
import sys
import io
from datetime import datetime

# Ensure UTF-8 output for Windows terminals
if sys.platform == "win32":
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

def load_data(file_path):
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"Data file not found: {file_path}")
    with open(file_path, 'r', encoding='utf-8') as f:
        return json.load(f)

def calculate_ration(data, animal_breed, ration_mix, export_path=None):
    # Find animal requirement
    breed_data = None
    category_found = None
    for category in ['cattle', 'sheep']:
        if animal_breed.lower() in data.get(category, {}):
            breed_data = data[category][animal_breed.lower()]
            category_found = category
            break
    
    if not breed_data:
        print(f"Error: Breed '{animal_breed}' not found in database.")
        return None

    results = {
        "metadata": {
            "project": "The Livestock Encyclopedia",
            "timestamp": datetime.now().isoformat(),
            "breed": animal_breed,
            "category": category_found
        },
        "formula": [],
        "summary": {}
    }

    print(f"\n" + "="*70)
    print(f"THE LIVESTOCK ENCYCLOPEDIA - RATION ANALYSIS: {animal_breed.upper()}")
    print("="*70)
    
    target_cp = breed_data.get('lactation_cp_pct', breed_data.get('growth_cp_pct'))
    print(f"TARGET PARAMETERS: CP: {target_cp}% | Energy: {breed_data['energy_mcal_kg']} Mcal")
    print("-" * 70)

    total_as_fed_weight = 0
    total_dm_weight = 0
    total_cp_weight = 0
    total_energy = 0
    total_cost = 0

    print(f"{'Feed Name':22} | {'AsFed(kg)':9} | {'DM(kg)':7} | {'CP%':5} | {'Cost(TL)':8}")
    print("-" * 70)

    for feed_name, weight_kg in ration_mix.items():
        feed_info = next((f for f in data['feeds'] if f['name'].lower() == feed_name.lower()), None)
        if not feed_info:
            print(f"Warning: Feed '{feed_name}' not found.")
            continue
        
        dm_kg = weight_kg * (feed_info['dm_pct'] / 100.0)
        cp_kg = dm_kg * (feed_info['cp_pct_dm'] / 100.0)
        energy_mcal = dm_kg * feed_info['energy_mcal_kg_dm']
        cost = (feed_info.get('cost_per_ton_as_fed', 0) / 1000.0) * weight_kg
        
        total_as_fed_weight += weight_kg
        total_dm_weight += dm_kg
        total_cp_weight += cp_kg
        total_energy += energy_mcal
        total_cost += cost
        
        row = {
            "name": feed_info['name'],
            "as_fed_kg": round(weight_kg, 2),
            "dm_kg": round(dm_kg, 2),
            "cp_pct_dm": feed_info['cp_pct_dm'],
            "cost_tl": round(cost, 2)
        }
        results["formula"].append(row)
        print(f"{row['name']:22} | {row['as_fed_kg']:9.1f} | {row['dm_kg']:7.2f} | {row['cp_pct_dm']:5.1f} | {row['cost_tl']:8.2f}")

    final_cp_pct = (total_cp_weight / total_dm_weight * 100.0) if total_dm_weight > 0 else 0
    final_energy_avg = (total_energy / total_dm_weight) if total_dm_weight > 0 else 0
    cost_per_kg_dm = total_cost / total_dm_weight if total_dm_weight > 0 else 0

    results["summary"] = {
        "total_as_fed_kg": round(total_as_fed_weight, 2),
        "total_dm_kg": round(total_dm_weight, 2),
        "cp_pct": round(final_cp_pct, 2),
        "target_cp_pct": target_cp,
        "energy_mcal_kg": round(final_energy_avg, 2),
        "target_energy_mcal_kg": breed_data['energy_mcal_kg'],
        "total_daily_cost_tl": round(total_cost, 2),
        "cost_per_kg_dm_tl": round(cost_per_kg_dm, 2)
    }

    print("-" * 70)
    print(f"SUMMARY RESULTS")
    print("-" * 70)
    print(f"Total Weight (As Fed):   {results['summary']['total_as_fed_kg']:8.2f} kg")
    print(f"Total Dry Matter (DM):   {results['summary']['total_dm_kg']:8.2f} kg")
    print(f"Ration Crude Protein:    {results['summary']['cp_pct']:8.2f} %  (Target: {target_cp}%)")
    print(f"Ration Net Energy:       {results['summary']['energy_mcal_kg']:8.2f} Mcal/kg (Target: {breed_data['energy_mcal_kg']} Mcal)")
    print(f"Total Daily Cost:        {results['summary']['total_daily_cost_tl']:8.2f} TL")
    print(f"Cost per kg DM:          {results['summary']['cost_per_kg_dm_tl']:8.2f} TL")
    print("=" * 70)
    
    # Interpretation
    diff_cp = final_cp_pct - target_cp
    if abs(diff_cp) < 0.5:
        print("\n[RESULT] CP Balance: BALANCED (Dengeli)")
    else:
        status = "HIGH" if diff_cp > 0 else "LOW"
        print(f"\n[RESULT] CP Balance: {status} ({diff_cp:+.2f}%)")

    if export_path:
        with open(export_path, 'w', encoding='utf-8') as f:
            json.dump(results, f, indent=4, ensure_ascii=False)
        print(f"\n[OK] Report exported to: {export_path}")

    return results

def main():
    parser = argparse.ArgumentParser(description="Precision Ration Calculator for The Livestock Encyclopedia.")
    parser.add_argument("--breed", type=str, default="holstein", help="Animal breed (e.g., holstein, jersey, angus)")
    parser.add_argument("--mix", type=str, help="JSON string for ration mix. Key: Feed Name, Value: Weight in KG.")
    parser.add_argument("--export", type=str, help="Path to export the result as JSON.")
    parser.add_argument("--list-feeds", action="store_true", help="List available feeds in the database.")
    parser.add_argument("--list-breeds", action="store_true", help="List available breeds in the database.")

    args = parser.parse_args()

    DATA_PATH = os.path.join(os.path.dirname(__file__), '..', 'data', 'standard_requirements.json')
    try:
        data = load_data(DATA_PATH)
        
        if args.list_feeds:
            print("\nAVAILABLE FEEDS:")
            for f in data['feeds']:
                print(f"- {f['name']} (CP: {f['cp_pct_dm']}%, DM: {f['dm_pct']}%)")
            return

        if args.list_breeds:
            print("\nAVAILABLE BREEDS:")
            for cat in ['cattle', 'sheep']:
                print(f"[{cat.upper()}]")
                for b in data[cat]:
                    print(f"- {b}")
            return

        if args.mix:
            mix = json.loads(args.mix)
        else:
            # Default example if no mix provided
            print("\n[INFO] No mix provided. Running default scenario (High-producing Holstein).")
            mix = {
                "Corn Silage": 22.0,
                "Alfalfa Silage": 6.0,
                "Soybean Meal": 4.5,
                "Barley Grain": 7.0,
                "Cottonseed Meal": 2.5
            }
        
        calculate_ration(data, args.breed, mix, args.export)
        
    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()

