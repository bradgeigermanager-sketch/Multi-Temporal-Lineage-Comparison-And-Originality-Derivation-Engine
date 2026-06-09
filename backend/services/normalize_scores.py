def normalize_scores(candidates):
    total_score = sum(c['score'] for c in candidates)
    if total_score == 0: return candidates
    
    for c in candidates:
        c['probability'] = c['score'] / total_score
    return candidates
