import hashlib

def sha256(data):
    if isinstance(data, str):
        data = data.encode('utf-8')
    return hashlib.sha256(data).hexdigest()

leaves = ['a', 'b', 'f', 'd']

hashed_leaves = [sha256(leaf) for leaf in leaves]

# print the original leaves and their hashed values
'''print("Hashed Leaves: ")
for i, h in enumerate(hashed_leaves):
    print(f"Leaf {i} {(leaves[i])}: {h}")
'''
def build_merkle_tree(hashed_leaves):
    tree = [hashed_leaves]
    while len(tree[0]) > 1:
        current_level = tree[0]
        next_level = []

        # If the current level has an odd number of nodes, duplicate the last node
        if len(current_level) % 2 == 1:
            current_level.append(current_level[-1])
        
        # Hash pairs of nodes to create the next level
        for i in range(0, len(current_level), 2):
            left = current_level[i]
            right = current_level[i+1]
            parent_hash = sha256(left + right)
            next_level.append(parent_hash)
        tree.insert(0, next_level)
    return tree

tree = build_merkle_tree(hashed_leaves)

'''
print("Merkle Tree: ")
for level_index, level in enumerate(tree):
    print(f"level {level_index}: ")
    for node in level:
        print(" ", node)
'''

def get_merkle_proof(tree, leaf_index):
    proof = []

    level_index = len(tree) - 1 # the last level contains the leaves

    while level_index > 0:
        level = tree[level_index]
        is_right_node = leaf_index % 2 == 1
        sibling_index = leaf_index - 1 if is_right_node else leaf_index + 1
        if sibling_index < len(level):
            sibling_hash = level[sibling_index]
            direction = 'left' if is_right_node else 'right'
            proof.append((sibling_hash, direction))

        # update the leaf index of node father level
        leaf_index = leaf_index // 2
        level_index -= 1
    return proof
        
# leaf_index = 0
# proof = get_merkle_proof(tree, leaf_index)
# print("Merkle proof for leaf index 0: ")
# for sibling_hash, direction in proof:
#     print(f"Sibling ({direction}): {sibling_hash[:8]}...")

def verify_merkle_proof(leaf_data, proof, expected_root):
    current_hash = sha256(leaf_data)
    for sibling_hash, direction in proof:
        if direction == 'left':
            current_hash = sha256(sibling_hash + current_hash)
        else:
            current_hash = sha256(current_hash + sibling_hash)
    return current_hash == expected_root

leaf_index = 2
leaf_value = leaves[leaf_index]
proof = get_merkle_proof(tree, leaf_index)
merkle_root = tree[0][0]

result = verify_merkle_proof(leaf_value, proof, merkle_root)
print(f"Verification result for leaf index {leaf_index}: {result}")