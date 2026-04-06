import json
import os

def load_data(file_path):
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"Data file not found: {file_path}")
    with open(file_path, 'r', encoding='utf-8') as f:
        return json.load(f)

def calculate_ration(data, animal_breed, ration_mix):
    # Find animal requirement
    breed_data = None
    for category in ['cattle', 'sheep']:
        if animal_breed.lower() in data.get(category, {}):
            breed_data = data[category][animal_breed.lower()]
            break
    
    if not breed_data:
        print(f"Error: Breed '{animal_breed}' not found in data.")
        return

    print(f"\n" + "="*60)
    print(f"THE LIVESTOCK ENCYCLOPEDIA - RATION ANALYSIS: {animal_breed.upper()}")
    print("="*60)
    
    target_cp = breed_data.get('lactation_cp_pct', breed_data.get('growth_cp_pct'))
    print(f"TARGET PARAMETERS: CP: {target_cp}% | Energy: {breed_data['energy_mcal_kg']} Mcal")
    print("-" * 60)

    total_as_fed_weight = 0
    total_dm_weight = 0
    total_cp_weight = 0
    total_energy = 0
    total_cost = 0

    print(f"{'Feed Name':18} | {'AsFed(kg)':9} | {'DM(kg)':7} | {'CP%':5} | {'Cost(TL)':8}")
    print("-" * 60)

    for feed_name, weight_kg in ration_mix.items():
        feed_info = next((f for f in data['feeds'] if f['name'] == feed_name), None)
        if not feed_info:
            print(f"Warning: Feed '{feed_name}' not found.")
            continue
        
        dm_kg = weight_kg * (feed_info['dm_pct'] / 100.0)
        cp_kg = dm_kg * (feed_info['cp_pct_dm'] / 100.0)
        energy = dm_kg * feed_info['energy_mcal_kg_dm']
        
        # Calculate cost: cost per ton / 1000 * kg as fed
        cost = (feed_info.get('cost_per_ton_as_fed', 0) / 1000.0) * weight_kg
        
        total_as_fed_weight += weight_kg
        total_dm_weight += dm_kg
        total_cp_weight += cp_kg
        total_energy += energy
        total_cost += cost
        
        print(f"{feed_name:18} | {weight_kg:9.1f} | {dm_kg:7.2f} | {feed_info['cp_pct_dm']:5.1f} | {cost:8.2f}")

    final_cp_pct = (total_cp_weight / total_dm_weight * 100.0) if total_dm_weight > 0 else 0
    final_energy_avg = (total_energy / total_dm_weight) if total_dm_weight > 0 else 0
    cost_per_kg_dm = total_cost / total_dm_weight if total_dm_weight > 0 else 0

    print("-" * 60)
    print(f"SUMMARY RESULTS")
    print("-" * 60)
    print(f"Total Weight (As Fed): {total_as_fed_weight:8.2f} kg")
    print(f"Total Dry Matter (DM): {total_dm_weight:8.2f} kg")
    print(f"Ration Crude Protein: {final_cp_pct:8.2f} %  (Target: {target_cp}%)")
    print(f"Ration Net Energy:    {final_energy_avg:8.2f} Mcal/kg (Target: {breed_data['energy_mcal_kg']} Mcal)")
    print(f"Total Daily Cost:     {total_cost:8.2f} TL")
    print(f"Cost per kg DM:       {cost_per_kg_dm:8.2f} TL")
    print("=" * 60)
    
    # Interpretation
    diff_cp = final_cp_pct - target_cp
    if abs(diff_cp) < 0.5:
        print("\n[RESULT] CP Balance: BALANCED (Dengeli)")
    else:
        status = "HIGH" if diff_cp > 0 else "LOW"
        print(f"\n[RESULT] CP Balance: {status} ({diff_cp:+.2f}%)")

if __name__ == "__main__":
    DATA_PATH = os.path.join(os.path.dirname(__file__), '..', 'data', 'standard_requirements.json')
    try:
        content = load_data(DATA_PATH)
        
        # Scenario: High-producing Holstein Dairy Cow
        my_mix = {
            "Corn Silage": 22.0,
            "Alfalfa Silage": 6.0,
            "Soybean Meal": 4.5,
            "Barley Grain": 7.0,
            "Cottonseed Meal": 2.5
        }
        
        calculate_ration(content, "holstein", my_mix)
        
    except Exception as e:
        print(f"Error: {e}")
