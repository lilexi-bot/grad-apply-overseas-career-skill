# Example: Evidence Map (FICTIONAL sample — do not reuse as your own)

> This demonstrates the expected depth. All names, numbers and projects below are invented for illustration.

## Entry E02 — "RT-Chain" real-time BFT consensus prototype
- **Timeline:** 2025.03 – 2025.11 · research project, Distributed Systems Lab
- **Type:** research + open-source
- **Problem:** existing BFT consensus (HoneyBadger-class) has unbounded latency on bursty workloads; CPS/edge control loops need bounded tail latency.
- **Technical stack:** Go, RDMA verbs, CXL memory pooling; randomised Byzantine agreement; P4 testbed with 32 emulated nodes, f=10.
- **What I did:** designed the epoch-based random-leader rotation; implemented the RDMA broadcast path; built the fault-injection harness.
- **Quantified results:** p99 commit latency 11.8ms vs PBFT 47ms under f=10 attack load; throughput 84k tx/s (2.1x baseline); code open-sourced, 340 stars.
- **Artifacts:** github.com/example/rt-chain; workshop demo award; paper under HPDC 2026 submission.
- **Reflection & linkage:** learned that consensus research must co-design with the memory/storage layer — motivates applying to systems-heavy MSCS programmes; also the seed of a hard-tech venture thesis (deterministic infra for real-time AI agents).
- **Reusable tags:** #cs #systems #founder #research

## Venture add-on (example)
- Entity: RTChain Labs Inc., Delaware C-Corp, incorporated 2026.02; ownership 65% founder / 20% co-founder / 15% option pool
- Traction: 2 paying pilot customers (robotics fleet operators), $8k MRR, waitlist 40 teams
- Funding: $150k pre-seed SAFE from an alumni angel (2026.05); applying YC W27
- IP: provisional patent filed on bounded-latency consensus (US, 2026.06)
- Visa mapping: IER needs $311k qualified-US-investor raise → YC SAFE could qualify; gap today = investor track record documentation; O-1A press coverage gap (2 articles → need 4+).
