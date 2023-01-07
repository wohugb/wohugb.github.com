# faq

!!! question "Mac 如果有有两个 git"

    :ref: https://apple.stackexchange.com/questions/93002/how-to-use-the-homebrew-installed-git-on-mac

    ```sh
    where git
    /usr/local/bin/git
    /usr/bin/git

    code ~/.zshrc
    add
    export PATH="/usr/local/bin:${PATH}"
    source ~/.zshrc
    git version
    ```
