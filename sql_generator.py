class SQLGenerator:
    def _init_(self):
        self.table_name = "STUDENT"
 def generate(self, intent, entities):
        """
        Maps an intent and extracted entities to a valid SQLite query.
        Returns the raw SQL string or None if fallback.
        """
        if intent == "fallback":
            return None
   # Base query components
        select_clause = f"SELECT * FROM {self.table_name}"
        where_clause = ""
        order_limit_clause = ""
   # Build WHERE clause based on entities
        if entities["marks"] is not None and entities["condition"] is not None:
            where_clause = f" WHERE MARKS {entities['condition']} {entities['marks']}"
        
