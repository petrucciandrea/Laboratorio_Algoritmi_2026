import time
from datetime import datetime
import random
import os
from structures import List, ABR, AVL

def insert_linear_test(struttura, n):
    """
    Testa il caso peggiore inserendo 'n' elementi in ordine sequenziale (da 1 a n).
    Ritorna il tempo totale e l'array dei tempi cumulativi.
    """
    tempi_cumulativi = []
    tempo_iniziale = time.perf_counter()
    
    for i in range(1, n + 1):
        struttura.insert(i)
        tempi_cumulativi.append(time.perf_counter() - tempo_iniziale)
        
    tempo_totale = tempi_cumulativi[-1] if n > 0 else 0.0
    return tempo_totale, tempi_cumulativi

def run_all_benchmarks(num_selects, sizes):
    output_lines = []
    
    # Funzione helper per stampare a schermo e salvare nel file contemporaneamente
    def log(message):
        print(message)
        output_lines.append(message)

    # =========================================================
    # PARTE 1: CASO MEDIO (Costruzione Casuale + Ricerche)
    # =========================================================
    log("\n" + "="*90)
    log(f"CASO MEDIO: DATI CASUALI ({num_selects} ricerche per N) - {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    log("="*90)
    log(f"{'N Elements':<12} | {'Structure':<12} | {'Insert Time':<18} | {'Select Time':<18} | {'Rank Time':<18}")
    log("-"*90)
    
    for n in sizes:
        # Generazione dati casuali
        random_data = random.sample(range(1, n * 10), n)
        search_indices = [random.randint(1, n) for _ in range(num_selects)]
        search_keys = random.choices(random_data, k=num_selects)
        
        # --- TEST LISTA ---
        my_list = List()
        start_time = time.perf_counter()
        for val in random_data: my_list.insert(val)
        t_insert_list = time.perf_counter() - start_time
        
        start_time = time.perf_counter()
        for i in search_indices: my_list.select(i)
        t_select_list = time.perf_counter() - start_time
        
        start_time = time.perf_counter()
        for k in search_keys: my_list.rank(my_list.root, k)
        t_rank_list = time.perf_counter() - start_time
        
        log(f"{n:<12} | {'List':<12} | {t_insert_list:<16f} s | {t_select_list:<16f} s | {t_rank_list:<16f} s")
        
        # --- TEST ABR ---
        my_bst = ABR()
        start_time = time.perf_counter()
        for val in random_data: my_bst.insert(val)
        t_insert_bst = time.perf_counter() - start_time
        
        start_time = time.perf_counter()
        for i in search_indices: my_bst.select(my_bst.root, i)
        t_select_bst = time.perf_counter() - start_time
        
        start_time = time.perf_counter()
        for k in search_keys: my_bst.rank(my_bst.root, k)
        t_rank_bst = time.perf_counter() - start_time
        
        log(f"{n:<12} | {'ABR':<12} | {t_insert_bst:<16f} s | {t_select_bst:<16f} s | {t_rank_bst:<16f} s")
        
        # --- TEST AVL ---
        my_avl = AVL()
        start_time = time.perf_counter()
        for val in random_data: my_avl.insert(val)
        t_insert_avl = time.perf_counter() - start_time
        
        start_time = time.perf_counter()
        for i in search_indices: my_avl.select(i)
        t_select_avl = time.perf_counter() - start_time
        
        start_time = time.perf_counter()
        for k in search_keys: my_avl.rank(k)
        t_rank_avl = time.perf_counter() - start_time
        
        log(f"{n:<12} | {'AVL':<12} | {t_insert_avl:<16f} s | {t_select_avl:<16f} s | {t_rank_avl:<16f} s")
        log("-" * 90)


    # =========================================================
    # PARTE 2: CASO PEGGIORE (Costruzione Sequenziale)
    # =========================================================
    log("\n" + "="*60)
    log(f"CASO PEGGIORE: INSERIMENTO LINEARE ORDINATO")
    log("="*60)
    log(f"{'N Elements':<12} | {'Structure':<12} | {'Insert Time (Worst)':<20}")
    log("-"*60)

    for n in sizes:
        # Test Lista
        lista = List()
        t_list, _ = insert_linear_test(lista, n)
        log(f"{n:<12} | {'List':<12} | {t_list:<16f} s")

        # Test ABR
        abr = ABR()
        t_abr, _ = insert_linear_test(abr, n)
        log(f"{n:<12} | {'ABR':<12} | {t_abr:<16f} s")

        # Test AVL
        avl = AVL()
        t_avl, _ = insert_linear_test(avl, n)
        log(f"{n:<12} | {'AVL':<12} | {t_avl:<16f} s")
        log("-" * 60)


    # =========================================================
    # SALVATAGGIO DEI DATI SU FILE
    # =========================================================
    script_dir = os.path.dirname(__file__)
    data_dir = os.path.join(script_dir, '..', 'data')
    os.makedirs(data_dir, exist_ok=True)
    file_path = os.path.join(data_dir, "benchmark_results.txt")
    
    with open(file_path, "a", encoding="utf-8") as f:
        f.write("\n\n" + "\n".join(output_lines))
        
    print(f"\n[INFO] Risultati completi (Medio + Peggiore) salvati in:\n{os.path.abspath(file_path)}")


if __name__ == "__main__":
    print("\n" + "="*50)
    print("-- BENVENUTO NEL TESTER DI STATISTICHE D'ORDINE --")
    print("="*50)
    
    try:
        size = int(input("Con quanti elementi vuoi partire (n,2n,4n,8n)? "))
        num = int(input("Quanti elementi casuali vuoi cercare in ogni test? "))
        array_dinamico = [size, size * 2, size * 4, size * 8]
        
        print(f"\nAvvio dei test continui con N = {array_dinamico}...")
        run_all_benchmarks(num, array_dinamico)
        
    except ValueError:
        print("\n[ERRORE] Devi digitare dei numeri interi validi. Riprova.")