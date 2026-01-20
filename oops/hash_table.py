class HashTable:
    def __init__(self):
        """Initialize the hash table with an empty collection dictionary."""
        self.collection = {}
    
    def hash(self, key):
        """
        Compute the hash value of a key by summing Unicode values of all characters.
        
        Args:
            key (str): The key to hash
            
        Returns:
            int: The hash value (sum of Unicode values)
        """
        return sum(ord(char) for char in key)
    
    def add(self, key, value):
        """
        Add a key-value pair to the hash table.
        
        Args:
            key (str): The key
            value: The value to store
        """
        hash_value = self.hash(key)
        
        # If this hash value doesn't exist yet, create a new nested dictionary
        if hash_value not in self.collection:
            self.collection[hash_value] = {}
        
        # Store the key-value pair in the nested dictionary
        self.collection[hash_value][key] = value
    
    def remove(self, key):
        """
        Remove a key-value pair from the hash table.
        
        Args:
            key (str): The key to remove
        """
        hash_value = self.hash(key)
        
        # Check if the hash value exists and the key exists in the nested dictionary
        if hash_value in self.collection and key in self.collection[hash_value]:
            del self.collection[hash_value][key]
            
            # If the nested dictionary is now empty, remove it
            if not self.collection[hash_value]:
                del self.collection[hash_value]
    
    def lookup(self, key):
        """
        Look up a value by key in the hash table.
        
        Args:
            key (str): The key to look up
            
        Returns:
            The value associated with the key, or None if not found
        """
        hash_value = self.hash(key)
        
        # Check if the hash value exists and the key exists in the nested dictionary
        if hash_value in self.collection and key in self.collection[hash_value]:
            return self.collection[hash_value][key]
        
        return None


# Example usage and testing
if __name__ == "__main__":
    # Create a new hash table
    ht = HashTable()
    
    # Test adding key-value pairs
    ht.add("name", "Alice")
    ht.add("age", 30)
    ht.add("city", "New York")
    
    # Test lookup
    print(f"Name: {ht.lookup('name')}")  # Output: Alice
    print(f"Age: {ht.lookup('age')}")    # Output: 30
    print(f"City: {ht.lookup('city')}")  # Output: New York
    
    # Test lookup for non-existent key
    print(f"Country: {ht.lookup('country')}")  # Output: None
    
    # Test hash collision (keys with same hash)
    print(f"\nHash of 'ab': {ht.hash('ab')}")  # 97 + 98 = 195
    print(f"Hash of 'ba': {ht.hash('ba')}")    # 98 + 97 = 195
    
    ht.add("ab", "value1")
    ht.add("ba", "value2")
    
    print(f"Lookup 'ab': {ht.lookup('ab')}")  # Output: value1
    print(f"Lookup 'ba': {ht.lookup('ba')}")  # Output: value2
    
    # Test remove
    ht.remove("name")
    print(f"\nAfter removing 'name': {ht.lookup('name')}")  # Output: None
    
    # Test removing non-existent key (should not raise error)
    ht.remove("nonexistent")
    
    # Display the collection structure
    print(f"\nHash table collection: {ht.collection}")
