# Bank of RASPUTIN (Core Banking System Engine)

A secure, high-integrity command-line banking interface built completely from scratch using pure Python. This project implements a modular software architecture featuring automated accounting ledger cross-checks, secure multi-tiered identity verification, and dynamic transactional fail-safes.

---

## ⚙️ Core Operational Logic

The system is engineered using **Modular Design Principles** to ensure a strict separation of concerns. Instead of a single monolithic script, the system splits infrastructure responsibilities across five interconnected layers that communicate via local scopes, function parameters, and explicit tuple returns.

* **State Management:** The application monitors accounts through distinct, predefined operational states (`"Status": "Active"` or `"Activity": "LOCKED"`). If any transaction violates business constraints or security parameters are exceeded, the account dynamically mutates its state to protect persistent records.
* **Data Flow Architecture:**
  1. `main.py` serves as the orchestrator, capturing terminal inputs and driving the console menu loops.
  2. `auth.py` acts as the security gateway, handling encrypted access matching and counting authentication thresholds.
  3. `engine.py` processes mathematical business rules isolated from user interfaces.
  4. `validators.py` calculates transaction histories to prevent unauthorized balance modifications.
  5. `storage.py` manages disk persistent input/output, parsing tracking matrices to `data.json`.

---

## 📊 Data Structures & Algorithms (DSA) Utilized

The system leverages fundamental data structures and algorithmic checks to manage data efficiently and maintain ledger accuracy:

### 1. Hash Maps / Dictionaries ($O(1)$ Time Complexity)
The system stores user records inside a nested JSON dictionary structure. The user's registration ID serves as the unique hash key.
* **Efficiency:** Account lookup, field updates, and credential validation scale at constant time, $O(1)$, entirely bypassing the need to iterate through the entire user base linearly.

### 2. Time-Ordered Sequential Arrays (Lists)
Every financial event modifies a continuous dynamic array containing delta tokens:
* **Format:** `[ "DD-MM-YYYY at HH:MM:SS | BalanceModifier[D/W]" ]`
* **Performance:** Appending records scales at $O(1)$ amortized complexity, allowing the ledger to grow infinitely while capturing full historic execution trails.

### 3. Linear Balance Reconstruction Algorithm ($O(N)$ Space-Time)
Before saving any state change to disk, an integrated validator executes an auditing algorithm that dynamically recalculates historical tokens:

$$\text{Reconstructed Balance} = \sum(\text{Deposits}) - \sum(\text{Withdrawals})$$

The engine parses the entire array list linearly, extracting and evaluating string tokens to confirm that the computed delta exactly matches the current state variable stored under the `"balance"` key.

---

## 💎 The Best Feature: Atomic Transaction Rollback

The standout mechanism within this system is its **Defensive Programming Layer** and **Atomic Failure Protection**. 

Financial software must never accept partial or unverified state modifications. If a user attempts to execute a deposit or withdrawal, the math is first tentatively performed on local memory, and a string token is appended to the historical log array. 

Immediately following this change, the ledger balance checker triggers. If any processing anomaly, numerical tampering, or drift is caught during verification:
1. The engine triggers an immediate rollback sequence.
2. The contaminated array index is instantly removed using a `.pop()` operation.
3. The user balance key reverts to a cached, pre-transaction state variable.
4. Disk write mechanisms inside `storage.py` are safely bypassed, preventing database corruption.

---

## 🚀 Capabilities & System Features

* **Real-Time Audit Verification:** Automatically catches database manual modification or programmatic data mismatching before modifying persistence blocks.
* **Persistent Local Database Engine:** Coordinates robust reading and formatting of disk states, cleanly writing data back with formatted, human-readable currency representations.
* **Multi-Tier Identity Defrosting Layer:** Implements locked security state routing. If an account is locked out from standard login attempts, it requires alternative admin bypass inputs or matching targeted key-value Security Questions.
* **Granular Input Sanitization:** Shields financial operations from breaking runtime logic errors by wrapping string/float conversions in structural try-except blocks.

---

## 🛠️ Local Setup & Execution Guide

1. Clone the project repository.
2. Ensure your directory structure matches this layout:
   ```text
   📁 rasputin-bank/
   │── 📄 main.py
   │── 📄 data.json
   └── 📁 core/
       │── 📄 __init__.py
       │── 📄 auth.py
       │── 📄 engine.py
       │── 📄 storage.py
       └── 📄 validators.py