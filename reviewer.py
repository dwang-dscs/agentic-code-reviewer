from harvester import get_git_diff

def generate_review(diff_text):
    if not diff_text.strip():
        return "No new code changes to review."

    system_prompt = (
        "You are a Senior Software Engineer. Review the following code changes "
        "for bugs, efficiency, and readability. Be concise and professional."
    )
    
    full_prompt = f"{system_prompt}\n\nCODE TO REVIEW:\n{diff_text}"
    
    return full_prompt

if __name__ == "__main__":
    new_code = get_git_diff()
    print("--- AI REVIEW PROMPT GENERATED ---")
    print(generate_review(new_code))