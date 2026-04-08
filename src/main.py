import time
import random
import os
from structures import List, ABR, AVL

def run_benchmark():
    # Define the input sizes to test
    sizes = [1000, 2000, 4000, 8000]
    num_selects = 100  # Number of searches to perform for each test
    
    # List to store all text lines to save in the file
    output_lines = []
    
    # Helper function: prints to screen and appends to output_lines
    def log(message):
        print(message)
        output_lines.append(message)
    
    log("="*75)
    log(f"COMPARISON TEST: DYNAMIC ORDER STATISTICS ({num_selects} searches per N)")
    log("="*75)
    log(f"{'N Elements':<12} | {'Structure':<12} | {'Insert Time':<20} | {'Select Time':<20}")
    log("-" * 75)
    
    for n in sizes:
        # 1. Generate N unique random numbers
        random_data = random.sample(range(1, n * 10), n)
        search_indices = [random.randint(1, n) for _ in range(num_selects)]
        
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
        
        log(f"{n:<12} | {'List':<12} | {t_insert_list:<17.5f} s | {t_select_list:<17.5f} s")
        
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
        
        log(f"{n:<12} | {'BST':<12} | {t_insert_bst:<17.5f} s | {t_select_bst:<17.5f} s")
        
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
        
        log(f"{n:<12} | {'AVL (Aug.)':<12} | {t_insert_avl:<17.5f} s | {t_select_avl:<17.5f} s")
        log("-" * 75)

    # 4. Save to text file
    # Get the absolute path of the 'data' directory, which is 
    # one level above where this script is located (src)
    script_dir = os.path.dirname(__file__)
    data_dir = os.path.join(script_dir, '..', 'data')
    
    # Ensure the 'data' directory exists (even if it's already there)
    os.makedirs(data_dir, exist_ok=True)
    
    # Create the full file path
    file_path = os.path.join(data_dir, "benchmark_results.txt")
    
    with open(file_path, "w", encoding="utf-8") as f:
        f.write("\n".join(output_lines))
        
    print(f"\n[INFO] Results successfully saved in:\n{os.path.abspath(file_path)}")

if __name__ == "__main__":
    run_benchmark()