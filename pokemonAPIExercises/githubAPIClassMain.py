import githubAPIClass

def main():
    github = githubAPIClass.GitHubAPI("CarlosOlvera05")
    user_data = github.get_user_data()
    repositories = github.get_repositories()
    
    print(f"Login: {user_data['login']}")
    print(f"Repos: {len(repositories)}")
    
if __name__ == "__main__":
    main()