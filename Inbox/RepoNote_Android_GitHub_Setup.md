# Android 使用 RepoNote 同步 GitHub

## 1. 准备 GitHub 仓库
- 登录 [GitHub](https://github.com/)。
- 创建或选择自己的仓库，建议设置为 **Private**。
- 确认当前账号有该仓库的访问权限。

## 2. 创建访问令牌（Token）
打开 [GitHub Fine-grained Tokens](https://github.com/settings/personal-access-tokens/new)，设置：

- **Token name**：`RepoNote`
- **Resource owner**：选择仓库所属用户或组织
- **Repository access**：选择 `Only select repositories`，勾选目标仓库
- **Repository permissions**：
  - `Contents`：**Read and write**
  - `Metadata`：**Read-only**（通常自动设置）
- **User permissions**：通常无需额外设置

创建后立即复制 Token，妥善保存，不要分享给别人。

## 3. 配置 RepoNote
1. 在 Android 安装并打开 RepoNote。
2. 使用 GitHub Token 连接账号。
3. 选择目标仓库、分支和笔记目录。
4. 选择仓库根目录作为 Vault，或指定一个文件夹。

## 4. 验证同步
1. 新建一篇 Markdown 笔记。
2. 输入几行测试内容，等待自动同步。
3. 打开 GitHub 仓库，确认文件已上传。

## 5. 如果提示没有权限
出现 `You don't have permission for the selected repository` 时，检查：

- Token 是否授权了正确的仓库。
- `Contents` 是否为 `Read and write`。
- `Resource owner` 是否正确。
- RepoNote 是否已更新为新 Token。

**注意：** 不要将 Token 写进笔记或提交到仓库。首次使用时先测试同步成功，再存放重要内容。
