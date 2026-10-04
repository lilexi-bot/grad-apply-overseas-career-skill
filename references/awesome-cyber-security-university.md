# Awesome Cyber Security University — 免费网络安全自学课程体系

> **导读 (Agent Read-First)**
>
> - **When to load:** 用户对网络安全/渗透测试/红蓝队感兴趣，或想寻找免费动手实践的安全学习资源时
> - **Trigger:** cybersecurity university red team blue team TryHackMe pentesting 渗透测试 红队 蓝队 CTF 网络安全学习 免费安全课程 awesome cyber security OWASP reverse engineering forensics
> - **Source:** [brootware/awesome-cyber-security-university](https://github.com/brootware/awesome-cyber-security-university)（GitHub ⭐3.2k）
> - **Keywords:** free cybersecurity curriculum, red team path, blue team path, TryHackMe, CTF, OWASP, privilege escalation, reverse engineering, digital forensics, SIEM

---

## 平台简介

**Awesome Cyber Security University** 是一个由 [brootware](https://github.com/brootware) 维护的免费网络安全教育资源合集，核心理念是 "learn by doing"（动手实践），所有资源均基于 [TryHackMe](https://tryhackme.com) 平台的免费房间。

- **Stars:** 3.2k | **License:** CC0-1.0（完全自由使用）
- **官网:** https://brootware.github.io/awesome-cyber-security-university/

---

## 课程体系（6大模块，难度线性递进）

### 模块1：Introduction & Pre-Security（入门预备）
- OpenVPN 连接、THM 平台使用、研究方法论
- Linux Fundamentals 1/2/3（Linux 基础命令）
- 渗透测试基础、信息安全原则、红队行动概览
- 入门 CTF：Google Dorking、OSINT、Shodan.io

### 模块2：Free Beginner Red Team Path（红队初学者路径）

| Level | 主题 | 核心内容 |
|-------|------|---------|
| L2 | Tooling | tmux、Nmap/Curl/Netcat、Web Scanning、子域枚举、Metasploit、Hydra |
| L3 | Crypto & Hashes | 哈希破解、Agent Sudo、The Cod Caper、Ice（Windows media server）、Lazy Admin |
| L4 | Web | OWASP Top 10、LFI、命令注入、JuiceShop、Overpass、Year of the Rabbit |
| L5 | Reverse Engineering & Pwn | x64 Assembly、Ghidra、Radare2、ELF逆向、Router Firmware、pwntools、Pwnkit CVE-2021-4034 |
| L6 | PrivEsc | Sudo CVE-2019-14287/18634、Windows/Linux Privesc Arena、Buffer Overflow |

### 模块3：Free Beginner Blue Team Path（蓝队初学者路径）

| Level | 主题 | 核心内容 |
|-------|------|---------|
| L1 | Tools | Windows Fundamentals、Nessus、MITRE ATT&CK、SIEM、Yara、OpenVAS、蜜罐、Volatility、Redline、Autopsy |
| L2 | SOC & Incident Response | Wireshark流量分析、Splunk Boss of the SOC V1/V2/V3、威胁狩猎（MITRE Tactics: Execution/Credential Access/Persistence/Defense Evasion） |
| L3 | Forensics & Crypto | 包分析（Packets Primer/Wireshark系列）、隐写术、编码解码 |
| L4 | Memory & Disk Forensics | 内存取证、磁盘取证进阶 |
| L5 | Malware & Reverse Engineering | 恶意软件历史、恶意软件逆向基础、PDF恶意文档分析 |

### 模块4：Bonus CTF Practice & Latest CVEs
- Bandit（Linux远程服务器入门）、Natas（Web安全基础）
- 后渗透基础（Mimikatz/BloodHound/PowerView/msfvenom）
- Docker逃逸、Kubernetes利用（Grafana LFI）、Spring4Shell CVE-2022-22965

### 模块5：Extremely Hard Rooms
- CCT2019（美国海军网络安全竞赛团队挑战）

---

## 学习建议

1. **按顺序来**：任务按难度线性排列，建议顺序完成，但可跳过已掌握的概念
2. **Red vs Blue 选择**：
   - 偏攻击/渗透 → Red Team Path
   - 偏防御/安全运营 → Blue Team Path
   - 两者都学最佳（攻防一体）
3. **完成徽章**：路径中隐藏了完成徽章代码，完成后可以展示在 GitHub profile
4. **全部免费**：所有资源均基于 TryHackMe 免费房间

---

## 与仓库其他资源的关系

- **安全方向职业路径**：可作为安全方向实习/工作的技能储备，补充海外安全岗位申请
- **AI安全交叉**：AI安全（AI Safety）日益重要，本路径提供底层安全理解基础
- **系统安全研究**：对分布式系统/拜占庭容错方向，安全视角是重要补充（攻击者模型、威胁建模）

---

**仓库：** https://github.com/brootware/awesome-cyber-security-university  
**在线版：** https://brootware.github.io/awesome-cyber-security-university/
