"""
Filter manuscript_statistics.json to contain only Phase 1 papers.
Protects unreleased papers (P000, P002, P006, P008, P010, P012-P045).

Phase 1 Papers: P001, P003, P004, P005, P007, P009, P011
"""

import json
from pathlib import Path

# Phase 1 papers for public release
PHASE_1_PAPERS = ['P001', 'P003', 'P004', 'P005', 'P007', 'P009', 'P011']

def filter_phase1_data():
    """Filter manuscript_statistics.json to Phase 1 papers only."""
    
    # File paths
    data_dir = Path(__file__).parent.parent / 'data'
    input_file = data_dir / 'manuscript_statistics.json'
    output_file = data_dir / 'manuscript_statistics_phase1.json'
    
    print(f"Reading: {input_file}")
    
    # Load full data
    with open(input_file, 'r', encoding='utf-8') as f:
        full_data = json.load(f)
    
    # Filter to Phase 1 papers only
    phase1_data = {}
    
    for paper_id, paper_data in full_data.items():
        if paper_id in PHASE_1_PAPERS:
            phase1_data[paper_id] = paper_data
            print(f"✅ Including: {paper_id} - {paper_data.get('title', 'No title')}")
        else:
            print(f"🔒 Protecting: {paper_id} (unreleased)")
    
    # Write filtered data
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(phase1_data, f, indent=2, ensure_ascii=False)
    
    print(f"\n✅ Created: {output_file}")
    print(f"📊 Phase 1 papers: {len(phase1_data)}/{len(full_data)} papers")
    print(f"🔒 Protected: {len(full_data) - len(phase1_data)} unreleased papers")
    
    return output_file

def create_paper_specific_files():
    """Create individual data files for each Phase 1 paper."""
    
    data_dir = Path(__file__).parent.parent / 'data'
    phase1_file = data_dir / 'manuscript_statistics_phase1.json'
    
    print(f"\nReading: {phase1_file}")
    
    with open(phase1_file, 'r', encoding='utf-8') as f:
        phase1_data = json.load(f)
    
    # Create paper-specific files
    for paper_id, paper_data in phase1_data.items():
        output_file = data_dir / f'manuscript_statistics_{paper_id}.json'
        
        with open(output_file, 'w', encoding='utf-8') as f:
            json.dump({paper_id: paper_data}, f, indent=2, ensure_ascii=False)
        
        print(f"✅ Created: manuscript_statistics_{paper_id}.json")
    
    print(f"\n✅ Created {len(phase1_data)} paper-specific data files")

if __name__ == '__main__':
    print("=" * 60)
    print("Phase 1 Data Protection Script")
    print("=" * 60)
    
    # Filter to Phase 1 only
    output_file = filter_phase1_data()
    
    # Create paper-specific files
    create_paper_specific_files()
    
    print("\n" + "=" * 60)
    print("✅ Data filtering complete!")
    print("=" * 60)
    print("\n📋 Next steps:")
    print("1. Verify manuscript_statistics_phase1.json contains only 7 papers")
    print("2. Update Public Data links in PHASE_1_SOCARXIV_ADAPTATION_CHECKLIST.md")
    print("3. Commit to GitHub before Days 5-10 submissions")
    print("4. Complete P005 Steps 5-6 submission with current links (acceptable)")
