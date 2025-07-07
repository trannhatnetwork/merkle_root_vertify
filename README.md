# 🌿 Merkle Tree Proof Verification

> A simple yet powerful Python project to **verify leaf membership** in a Merkle Tree — used in blockchain, cryptography, and distributed systems.

---

![Merkle Tree](https://upload.wikimedia.org/wikipedia/commons/thumb/9/95/Hash_Tree.svg/400px-Hash_Tree.svg.png)

<sup>Source: Wikipedia - Merkle Tree</sup>

---

## 🧠 Problem Statement

### **Goal:**
Given a list of values (like `["a", "b", "c", "d"]`), prove whether a specific value (e.g. `"a"`) truly exists in the list **without revealing the entire list**, using:

- ✅ A Merkle Tree  
- ✅ A Merkle proof  
- ✅ A known Merkle root

---

## 🚧 Exercise Requirements

- Implement SHA-256 based Merkle Tree
- Build the tree from a list of values
- Generate Merkle proof for a given index
- Verify that a value belongs to the tree using:
  - The value itself
  - Its proof path
  - And the root hash

---

## ❓ Theoretical Questions & Answers

### 🔸 What is a Merkle Tree?
A Merkle Tree is a binary tree where:
- Leaf nodes are hashes of individual data
- Non-leaf nodes are hashes of their children's concatenated hashes
- The topmost node (Merkle Root) summarizes the entire tree’s content

---

### 🔸 Why do we use Merkle Trees?
They help us verify the presence or integrity of data:
- Without revealing the full dataset  
- With very little information (just a few hashes)  
- In a scalable way (logarithmic proof size)

---

### 🔸 What is a Merkle proof?
It’s a minimal set of hashes + directions (left/right) that allows reconstructing the Merkle root from a given leaf node.

---

### 🔸 What if someone tampers with the data?
Any tampering will:
- Change one hash
- Break all hashes above it
- Result in a **wrong root**  
→ Proof will **fail**

---

### 🔸 Where is this used in the real world?
- ✅ Bitcoin, Ethereum, ZCash  
- ✅ Git (version control)  
- ✅ IPFS (distributed file systems)  
- ✅ zk-SNARKs and zero-knowledge proofs

---

## 📂 Solution

> 🧩 The full code with step-by-step explanation is available here:  
👉 [**View Solution**](https://github.com/your-username/your-repo/blob/main/merkle_proof_demo.py)

---

## 📚 Further Exploration

- 🔍 Try modifying the proof manually — does verification fail?
- 💡 Swap the leaf data — does the root match?
- 🛡 Implement Merkle Tree in reverse (rebuild the list from proof)
- 🔗 Learn about Merkle Patricia Trees (used in Ethereum)

---

## 🏁 Summary

This project helps you understand:
- ✅ How Merkle Trees are built  
- ✅ How data integrity can be verified efficiently  
- ✅ Why Merkle proofs are essential in blockchain and cryptography

---

> 🚀 Build secure systems by mastering the basics — this is one of them.
