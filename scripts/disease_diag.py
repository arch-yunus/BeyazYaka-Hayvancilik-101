#!/usr/bin/env python3
"""
disease_diag.py — THE LIVESTOCK ENCYCLOPEDIA
Expert System for Symptom-Based Disease Differential Diagnosis
"""

import json
import os
import argparse
import sys
import io

# Ensure UTF-8 output for Windows terminals
if sys.platform == "win32":
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

def load_database(file_path):
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"Database not found: {file_path}")
    with open(file_path, 'r', encoding='utf-8') as f:
        return json.load(f)

def diagnose(database, user_symptoms):
    results = []
    
    # Normalize user symptoms
    user_symptoms = [s.lower().strip() for s in user_symptoms]
    
    for disease in database['diseases']:
        match_count = 0
        matched_symptoms = []
        
        # Check for matches in disease symptoms
        disease_symptoms = [s.lower() for s in disease['symptoms']]
        
        for us in user_symptoms:
            # Check for partial matches too
            for ds in disease_symptoms:
                if us in ds or ds in us:
                    match_count += 1
                    matched_symptoms.append(ds)
                    break
        
        if match_count > 0:
            confidence = (match_count / len(disease['symptoms'])) * 100
            # Normalize confidence - if multiple user symptoms match few disease symptoms, don't exceed 100
            confidence = min(confidence, 100.0)
            
            results.append({
                "disease": disease,
                "match_count": match_count,
                "confidence": confidence,
                "matched_symptoms": list(set(matched_symptoms))
            })
            
    # Sort by confidence descending
    results.sort(key=lambda x: x['confidence'], reverse=True)
    return results

def print_diag_report(diagnoses):
    print("\n" + "="*80)
    print("  THE LIVESTOCK ENCYCLOPEDIA - HASTALIK ÖN TANI RAPORU (DIAGNOSTIC REPORT)")
    print("="*80)
    
    if not diagnoses:
        print("\n [!] Girdiğiniz semptomlarla eşleşen bir hastalık bulunamadı.")
        print(" [!] No matching diseases found for the provided symptoms.")
        return

    for i, d in enumerate(diagnoses[:5]): # Show top 5
        dis = d['disease']
        print(f"\n{i+1}. TANI: {dis['name'].upper()}")
        print(f"   Eşleşme Oranı (Confidence): %{d['confidence']:.1f}")
        print(f"   Tür: {dis['type']} | Zoonoz: {'EVET (DİKKAT!)' if dis['zoonotic'] else 'Hayır'}")
        print(f"   Eşleşen Semptomlar: {', '.join(d['matched_symptoms'])}")
        print("-" * 40)
        print(f"   Açıklama/Semptomlar: {', '.join(dis['symptoms'][:4])}...")
        print(f"   Korunma: {dis['prevention']}")
        
        if dis.get('zoonotic_note'):
            print(f"   ⚠️ NOT: {dis['zoonotic_note']}")
            
    print("\n" + "="*80)
    print(" UYARI: Bu araç sadece bilgilendirme amaçlıdır. Kesin tanı için VETERİNER HEKİM çağırmalısınız.")
    print(" WARNING: This is for educational purposes only. Consult a VETERINARIAN for definitive diagnosis.")
    print("="*80 + "\n")

def main():
    parser = argparse.ArgumentParser(description="Differential diagnosis tool based on symptoms.")
    parser.add_argument("symptoms", nargs="+", help="List of symptoms separated by spaces (e.g., 'ateş' 'topallık' 'salya')")
    parser.add_argument("--db", type=str, help="Path to disease_database.json.")
    
    args = parser.parse_args()
    
    db_path = args.db or os.path.join(os.path.dirname(__file__), '..', 'data', 'disease_database.json')
    
    try:
        db = load_database(db_path)
        results = diagnose(db, args.symptoms)
        print_diag_report(results)
        
    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
