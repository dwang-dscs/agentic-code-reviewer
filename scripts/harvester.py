import git

def get_git_diff(repo_path = '.'):
    try:
        repo = git.Repo(repo_path)

        diffs = repo.index.diff(None, create_patch = True)

        diff_text = ""

        for d in diffs:
            if d.change_type in ['M', 'A']:
                diff_text += f"--- File: {d.a_path} ---\n"

                patch_content = d.diff.decode('utf-8')

                added_lines = [line for line in patch_content.split('\n') if line.startswith('+') and not line.startswith('+++')]
                
                diff_text += "\n".join(added_lines) + "\n\n"

        return diff_text

    except Exception as e:
        return f"Error: {e}"

if __name__ == "__main__":
    changes = get_git_diff()
    if changes:
        print("Captured New Code Changes:\n")
        print(changes)
    else:
        print("No changes detected. Did you modify a file?")