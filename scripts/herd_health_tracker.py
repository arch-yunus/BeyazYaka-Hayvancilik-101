#!/usr/bin/env python3
"""
herd_health_tracker.py -- BeyazYaka Suru Saglik Kayit ve Uyari Sistemi
Basit CLI tabanli suru saglik veri yonetimi ve anomali uyarisi
"""

import json
import os
from datetime import date, datetime, timedelta
from dataclasses import dataclass, asdict
from typing import List, Optional

RECORDS_FILE = os.path.join(os.path.dirname(__file__), '..', 'data', 'herd_records.json')

@dataclass
class AnimalRecord:
    tag_id: str
    name: str
    breed: str
    birth_date: str
    last_calving: Optional[str] = None
    lactation_number: int = 0
    scc_last: int = 0
    bcs_last: float = 3.5
    health_events: List[str] = None

    def __post_init__(self):
        if self.health_events is None:
            self.health_events = []

class HerdHealthTracker:
    def __init__(self):
        self.records: List[AnimalRecord] = []
        self.load()

    def load(self):
        if os.path.exists(RECORDS_FILE):
            with open(RECORDS_FILE, 'r', encoding='utf-8') as f:
                raw = json.load(f)
                self.records = [AnimalRecord(**r) for r in raw]

    def save(self):
        with open(RECORDS_FILE, 'w', encoding='utf-8') as f:
            json.dump([asdict(r) for r in self.records], f, ensure_ascii=False, indent=2)

    def add_animal(self, animal: AnimalRecord):
        existing = [r for r in self.records if r.tag_id == animal.tag_id]
        if existing:
            print(f"[WARN] Hayvan {animal.tag_id} zaten kayitli!")
            return
        self.records.append(animal)
        self.save()
        print(f"[OK]   {animal.tag_id} - {animal.name} eklendi.")

    def record_health_event(self, tag_id: str, event: str):
        for r in self.records:
            if r.tag_id == tag_id:
                timestamp = datetime.now().strftime("%Y-%m-%d %H:%M")
                r.health_events.append(f"[{timestamp}] {event}")
                self.save()
                print(f"[LOG]  {tag_id} -> {event}")
                return
        print(f"[ERR]  Hayvan bulunamadi: {tag_id}")

    def update_scc(self, tag_id: str, scc: int):
        for r in self.records:
            if r.tag_id == tag_id:
                r.scc_last = scc
                if scc > 400000:
                    print(f"[!!!]  {tag_id}: SHS {scc:,} -> Mastitis suphesi! CMT testi yap.")
                elif scc > 200000:
                    print(f"[!!!]  {tag_id}: SHS {scc:,} -> Dikkat: Meme sagligi izle.")
                else:
                    print(f"[OK]   {tag_id}: SHS {scc:,} -> Normal.")
                self.save()
                return
        print(f"[ERR]  Hayvan bulunamadi: {tag_id}")

    def run_health_check(self):
        print("\n" + "=" * 60)
        print("  SURU SAGLIK DURUM RAPORU")
        print("=" * 60)
        alerts = []

        for r in self.records:
            if r.scc_last > 400000:
                alerts.append(f"[!!!] {r.tag_id} ({r.name}): SHS {r.scc_last:,} -- Mastitis riski!")
            elif r.scc_last > 200000:
                alerts.append(f"[!!]  {r.tag_id} ({r.name}): SHS {r.scc_last:,} -- Izle.")

            if r.bcs_last < 2.5:
                alerts.append(f"[!!!] {r.tag_id} ({r.name}): BCS {r.bcs_last} -- Ketosis riski! Enerji destegi yap.")
            elif r.bcs_last > 4.0:
                alerts.append(f"[!!]  {r.tag_id} ({r.name}): BCS {r.bcs_last} -- Asiri kondisyon, metritis riski.")

        if alerts:
            for a in alerts:
                print(f"  {a}")
        else:
            print("  [OK] Tum hayvanlar normal aralikta.")

        print(f"\n  Toplam {len(self.records)} bas | {sum(1 for r in self.records if r.scc_last > 200000)} mastitis riski")
        print("=" * 60)

    def summary(self):
        print(f"\n{'Kupe':>10} | {'Isim':>12} | {'Irk':>12} | {'Lak.':>5} | {'SHS':>10} | {'BCS':>5}")
        print("-" * 65)
        for r in self.records:
            scc_flag = "[!]" if r.scc_last > 400000 else ("[ ]" if r.scc_last > 200000 else "[+]")
            print(f"{r.tag_id:>10} | {r.name:>12} | {r.breed:>12} | {r.lactation_number:>5} | {scc_flag} {r.scc_last:>6,} | {r.bcs_last:>5.2f}")
        print()

def demo():
    tracker = HerdHealthTracker()

    animals = [
        AnimalRecord("TR-001", "Karabas",  "Holstein",    "2022-03-15", "2024-11-01", 2, 185000, 3.50),
        AnimalRecord("TR-002", "Sari",     "Holstein",    "2021-07-20", "2024-09-10", 3, 450000, 3.20),
        AnimalRecord("TR-003", "Benekli",  "Montbeliard", "2023-01-05", "2025-02-14", 1,  95000, 2.25),
        AnimalRecord("TR-004", "Dolma",    "Jersey",      "2020-05-12", "2025-01-20", 4, 780000, 3.80),
    ]

    for a in animals:
        tracker.add_animal(a)

    tracker.record_health_event("TR-002", "Sol on meme lobunda sertlik gozlemlendi. CMT: 2+. Vet cagirildi.")
    tracker.record_health_event("TR-004", "Klinik mastitis - E. coli. IV destekli AB baslandi.")

    tracker.summary()
    tracker.run_health_check()

if __name__ == "__main__":
    demo()
