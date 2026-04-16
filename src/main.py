import time
from datetime import datetime
import random
import os
from structures import List, ABR, AVL

def run_benchmark(num_selects, sizes):
    # List to store all text lines to save in the file
    output_lines = []
    
    # Helper function: prints to screen and appends to output_lines
    def log(message):
        print(message)
        output_lines.append(message)

    log("="*95)
    log(f"COMPARISON TEST: DYNAMIC ORDER STATISTICS ({num_selects} searches per N)")
    log(f"{datetime.now()}")
    log("="*95)
    log(f"{'N Elements':<12} | {'Structure':<12} | {'Insert Time':<18} | {'Select Time':<18} | {'Rank Time':<18}")
    log("-" * 95)
    
    for n in sizes:
        # 1. Generate N unique random numbers
        random_data = random.sample(range(1, n * 10), n)
        search_indices = [random.randint(1, n) for _ in range(num_selects)]
        search_keys = random.choices(random_data, k=num_selects)
        
        # ---------------------------------------------------------
        # TEST 1: SORTED LIST
        # ---------------------------------------------------------
        my_list = List()
        
        # Measure Insertion
        start_time = time.perf_counter()
        for val in random_data:
            my_list.insert(val)
        t_insert_list = time.perf_counter() - start_time
        
        # Measure Select
        start_time = time.perf_counter()
        for i in search_indices:
            my_list.select(i)
        t_select_list = time.perf_counter() - start_time
        
        # Measure Rank
        start_time = time.perf_counter()
        for k in search_keys:
            my_list.rank(my_list.root, k)
        t_rank_list = time.perf_counter() - start_time
        
        log(f"{n:<12} | {'List':<12} | {t_insert_list:<15.5f} s | {t_select_list:<15.5f} s | {t_rank_list:<15.5f} s")
        
        # ---------------------------------------------------------
        # TEST 2: STANDARD BST (Binary Search Tree)
        # ---------------------------------------------------------
        my_bst = ABR()
        
        # Measure Insertion
        start_time = time.perf_counter()
        for val in random_data:
            my_bst.insert(val)
        t_insert_bst = time.perf_counter() - start_time
        
        # Measure Select
        start_time = time.perf_counter()
        for i in search_indices:
            my_bst.select(my_bst.root, i)
        t_select_bst = time.perf_counter() - start_time
        
        # Measure Rank
        start_time = time.perf_counter()
        for k in search_keys:
            my_bst.rank(my_bst.root, k)
        t_rank_bst = time.perf_counter() - start_time
        
        log(f"{n:<12} | {'ABR':<12} | {t_insert_bst:<15.5f} s | {t_select_bst:<15.5f} s | {t_rank_bst:<15.5f} s")
        
        # ---------------------------------------------------------
        # TEST 3: AUGMENTED AVL
        # ---------------------------------------------------------
        my_avl = AVL()
        
        # Measure Insertion
        start_time = time.perf_counter()
        for val in random_data:
            my_avl.insert(val)
        t_insert_avl = time.perf_counter() - start_time
        
        # Measure Select
        start_time = time.perf_counter()
        for i in search_indices:
            my_avl.select(i)
        t_select_avl = time.perf_counter() - start_time
        
        # Measure Rank
        start_time = time.perf_counter()
        for k in search_keys:
            my_avl.rank(k)
        t_rank_avl = time.perf_counter() - start_time
        
        log(f"{n:<12} | {'AVL':<12} | {t_insert_avl:<15.5f} s | {t_select_avl:<15.5f} s | {t_rank_avl:<15.5f} s")
        log("-" * 95)

    # 4. Save to text file
    script_dir = os.path.dirname(__file__)
    data_dir = os.path.join(script_dir, '..', 'data')
    os.makedirs(data_dir, exist_ok=True)
    file_path = os.path.join(data_dir, "benchmark_results.txt")
    
    with open(file_path, "a", encoding="utf-8") as f:
        f.write("\n\n\n" + "\n".join(output_lines))
        
    print(f"\n[INFO] Results successfully saved in:\n{os.path.abspath(file_path)}")

if __name__ == "__main__":
    print("\n--- BENVENUTO NEL TESTER DI STATISTICHE D'ORDINE ---")
    try:
        size = int(input("Con quanti elementi vuoi partire (n,2n,4n,8n)? "))
        num = int(input("Quanti elementi casuali vuoi cercare in ogni test? "))
        array_dinamico = [size, size * 2, size * 4, size * 8]
        print(f"\nAvvio dei test con N = {array_dinamico} e {num} ricerche per ciclo...")
        run_benchmark(num, array_dinamico)
    except ValueError:
        print("[ERRORE] Devi digitare dei numeri interi validi. Riprova.")