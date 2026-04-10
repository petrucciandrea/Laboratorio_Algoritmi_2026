Petrucci, Andrea, 7050922, Esercizio 1: Statistiche d'ordine dinamiche

## 1. Descrizione del Progetto
Questo progetto implementa e confronta tre diverse strutture dati per la risoluzione del problema delle "Statistiche d'ordine dinamiche" (ricerca dell'i-esimo elemento più piccolo in un insieme dinamico). 
Le strutture analizzate sono:
* Lista Ordinata (implementazione con puntatori)
* Albero Binario di Ricerca (ABR Standard)
* Albero AVL Aumentato (con attributo 'size' per ottimizzare la ricerca)

## 2. Struttura della Repository
* /src: Contiene il codice sorgente Python (structures.py per le classi, main.py per il benchmark).
* /data: Contiene i risultati testuali generati durante l'esecuzione dei test (benchmark_results.txt).
* /latex: Contiene la relazione in formato LaTeX

## 3. Istruzioni per l'Esecuzione
Per avviare il benchmark interattivo e riprodurre i risultati dell'esperimento, posizionarsi nella root del progetto ed eseguire dal terminale: "python src/main.py"
All'avvio, il programma chiederà all'utente di inserire manualmente due parametri:
    1. La dimensione iniziale dell'insieme di dati.
    2. Il numero di ricerche casuali (select) da effettuare per ogni test.
Sulla base dell'input fornito, lo script genererà array di numeri casuali di dimensioni crescenti applicando il metodo del raddoppio (n, 2n, 4n, 8n).
Al termine dell'esecuzione automatizzata sulle tre strutture dati, i tempi di esecuzione e l'analisi della complessità asintotica verranno stampati e salvati in un report testuale all'interno della cartella /data.

## 4. Analisi dei Risultati e Complessità Asintotica
Dai test empirici condotti, emergono risultati in linea con le aspettative teoriche:
* Lista Ordinata: L'inserimento ordinato risulta estremamente costoso. La funzione 'select' richiede un tempo lineare dipendente dalla grandezza dei dati.
* ABR Standard: Le prestazioni migliorano rispetto alla lista, ma la funzione 'select', non avendo informazioni sulla dimensione dei sottoalberi, richiede comunque una visita in ordine dei nodi, risultando inefficiente al crescere dell'input.
* AVL Aumentato: Mantenendo il bilanciamento dell'altezza (garantendo l'inserimento logaritmico) e sfruttando l'attributo 'size' aggiornato dinamicamente tramite le rotazioni, la funzione 'select' esegue ricerche immediate "scartando" interi sottoalberi. Il tempo di ricerca si mantiene stabile e microscopico indipendentemente dalla crescita dell'input.