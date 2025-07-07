# 🧪 Merkle Tree Proof Verification

This project demonstrates how to verify whether a **leaf node** is a member of a given list using a **Merkle Tree** and its corresponding **Merkle proof**.

---

## 📌 Exercise Title

**"Verifying Leaf Membership in a Merkle Tree"**

---

## 🎯 Exercise Objectives

- Understand the structure and logic behind Merkle Trees.
- Build a Merkle Tree from a list of values.
- Generate a Merkle proof for any given leaf.
- Verify whether a leaf belongs to the original list using:
  - The leaf data,
  - The Merkle proof,
  - And the Merkle root.

---

## ❓ Theoretical Questions & Answers

### 🔸 What is a Merkle Tree?
A Merkle Tree is a binary tree data structure in which:
- Each **leaf node** represents the hash of a data element.
- Each **non-leaf node** is the hash of the concatenation of its two child nodes.
- The **root node** (Merkle root) represents the entire data structure.

---

### 🔸 Why do we need a Merkle proof?
A Merkle proof allows us to:
- Prove that a specific leaf is part of a larger dataset (the Merkle Tree),
- Without needing to store or transmit the entire tree or list.

This is especially useful in blockchain, distributed systems, or when verifying data integrity efficiently.

---

### 🔸 What does a Merkle proof contain?
A Merkle proof includes:
- A list of **sibling hashes** (called a proof path),
- Along with the **position** (left or right) of each sibling.

This is enough to **recompute the Merkle root** starting from the leaf node, and verify whether it matches the known root.

---

### 🔸 What happens if someone tampers with the data or the proof?
Any change in:
- The leaf value,
- A hash in the proof,
- Or the order (left/right) of the path

...will cause the computed Merkle root to differ from the expected root, and **the verification will fail**.

---

### 🔸 What real-world systems use Merkle Trees?
Merkle Trees are widely used in:
- **Blockchain** (e.g., Bitcoin, Ethereum),
- **Version control systems** (e.g., Git),
- **Distributed storage** (e.g., IPFS),
- **Cryptographic protocols** like ZK-SNARKs.

---

## 📂 Solution

> ✅ You can view the full step-by-step implementation here:  
> 👉 [**Click to see the solution**](https://github.com/your-username/your-repo/blob/main/merkle_proof_demo.py)

---

## 📌 Requirements Recap

- Input: a list of values (e.g., `["a", "b", "c", "d"]`)
- Output:
  - Build Merkle tree
  - Generate Merkle proof for a given index
  - Verify proof against root

---

## ✅ Notes

- Hashing algorithm used: `SHA-256`
- Language: Python 3
- No external libraries required

---

## 💡 Recommended Extension

Try modifying the proof manually and see if the verification fails — this helps solidify your understanding of **data integrity** and **proof correctness**.

---

