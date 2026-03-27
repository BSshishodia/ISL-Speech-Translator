def convert_to_isl(tokens):
    
    # Basic rule-based system
    remove_words = ["हूँ", "है", "था", "थी", "रहा", "रही", "रहे"]
    
    filtered = [word for word in tokens if word not in remove_words]
    
    # Example simple rule:
    # Move time words to front
    
    time_words = ["आज", "कल", "अभी"]
    
    time_part = [w for w in filtered if w in time_words]
    rest_part = [w for w in filtered if w not in time_words]
    
    isl_sentence = time_part + rest_part
    
    return isl_sentence