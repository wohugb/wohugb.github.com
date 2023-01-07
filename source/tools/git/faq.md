---
title: Git常见问题
---

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

!!! question "mac 解决一直弹出 git-credential-oskeychain 的问题"

    ++cmd+space++ 在搜索栏输入 Keychain Access, 在 `钥匙串` -> `登录` 删除 `github.com` 或者 `gitee.com`

    ![](https://img-blog.csdnimg.cn/img_convert/7f13598c560324fb2dd1e64f0313db1f.png)
