# ChainForensics — Presentation
> **Blockchain-Backed IoT Forensic Evidence Platform**

A technical and academic presentation documenting the design, implementation, validation, and forensic verification workflow of **ChainForensics** — a project that combines **IoT Security, Digital Forensics, and Blockchain** to create an independently verifiable evidence path for security-relevant IoT events.

---

## Table of Contents
- [Overview](#overview)
- [Project Context](#project-context)
- [Problem Statement](#problem-statement)
- [Core Idea](#core-idea)
- [Objectives](#objectives)
- [System Architecture](#system-architecture)
- [End-to-End Evidence Lifecycle](#end-to-end-evidence-lifecycle)
- [Technology Stack](#technology-stack)
- [IoT Edge Layer](#iot-edge-layer)
- [Evidence Ingestion](#evidence-ingestion)
- [Cryptographic Fingerprinting](#cryptographic-fingerprinting)
- [Evidence Preservation](#evidence-preservation)
- [Blockchain Evidence Anchoring](#blockchain-evidence-anchoring)
- [Forensic Verification](#forensic-verification)
- [Forensic Verdict Model](#forensic-verdict-model)
- [Threat Scenarios](#threat-scenarios)
- [Validation Results](#validation-results)
- [Forensic Independence](#forensic-independence)
- [Academic Contribution](#academic-contribution)
- [Presentation Structure](#presentation-structure)
- [Presentation Design System](#presentation-design-system)
- [Running the Presentation](#running-the-presentation)
- [Keyboard Controls](#keyboard-controls)
- [Repository Structure](#repository-structure)
- [Research Scope and Limitations](#research-scope-and-limitations)
- [Future Work](#future-work)
- [Important Technical Distinctions](#important-technical-distinctions)
- [Academic Positioning](#academic-positioning)
- [Acknowledgements](#acknowledgements)
- [License](#license)

---

## Overview

**ChainForensics** is a blockchain-backed IoT forensic evidence platform designed around one central question:

> **When an IoT system is compromised, can the evidence recorded by that system still be independently verified later?**

IoT environments continuously generate telemetry from sensors, edge devices, communication systems, gateways, and backend databases. During or after a security incident, these records may become difficult to trust because local evidence can be modified, deleted, replayed, or otherwise affected by compromise.

ChainForensics addresses this trust gap by creating a separation between:

- **Event generation**
- **Evidence processing**
- **Evidence preservation**
- **Cryptographic commitment**
- **Independent verification**

The complete evidence path is:

```text
IoT Security Event
        ↓
Structured Digital Evidence
        ↓
RFC 8785 Canonical Representation
        ↓
SHA-256 Evidence Digest
        ↓
Off-Chain Evidence Preservation
        ↓
Blockchain Commitment
        ↓
Later Evidence Reconstruction
        ↓
Independent Reconciliation
        ↓
Forensic Finding
```

The blockchain does not store the complete forensic evidence payload. Instead, it stores a compact cryptographic commitment that can later act as an independent reference.

---

## Project Context

ChainForensics sits at the intersection of three technical domains:

| Domain | Role in ChainForensics |
|---|---|
| IoT Security | Generates and contextualizes security-relevant events |
| Digital Forensics | Preserves, reconstructs, examines, and evaluates evidence |
| Blockchain | Provides an independent cryptographic reference |
| Cryptography | Produces deterministic evidence fingerprints |
| Distributed Systems | Separates evidence storage from trust verification |

The project is presented as a B.Tech capstone project under the School of Technology at Woxsen University.

---

## Problem Statement

Traditional IoT logging frequently relies on local databases, centralized services, device logs, or application-level audit mechanisms.

These approaches can create a forensic trust gap.

A compromised environment may allow an attacker or administrator with sufficient privileges to:

- Modify an existing record
- Delete evidence
- Replay an earlier event
- Manipulate event ordering
- Introduce an unauthorized device
- Make verification infrastructure temporarily unavailable
- Alter locally stored evidence without necessarily altering the original audit trail

The central forensic question becomes:

> How can a preserved IoT evidence record be independently verified after the originating system may no longer be fully trusted?

ChainForensics approaches this problem by maintaining an external cryptographic commitment that is separate from the complete evidence payload.

---

## Core Idea

The central architectural principle is:

> The local system stores the evidence. The blockchain provides the independent reference. The forensic verifier determines whether they still reconcile.

This creates three distinct responsibilities:

```text
IoT
│
├── Generates security-relevant events
│
Digital Forensics
│
├── Preserves and reconstructs evidence
│
Blockchain
│
└── Provides an external cryptographic commitment
```

The forensic verifier then compares:

```text
HASH_LOCAL
    ↕
HASH_ANCHOR
```

where:

- `HASH_LOCAL` = SHA-256 hash recalculated from reconstructed local evidence
- `HASH_ANCHOR` = trusted evidence commitment retrieved from blockchain state

---

## Objectives

**1. Security-Relevant IoT Event Generation**
Capture security-relevant conditions from an IoT edge environment and convert them into structured events.

**2. Deterministic Evidence Representation**
Validate and canonicalize security events before cryptographic fingerprinting.

**3. Evidence Preservation**
Preserve the complete evidence payload off-chain while maintaining provenance and retrieval information.

**4. Independent Cryptographic Reference**
Anchor a compact evidence commitment on a blockchain through a smart contract.

**5. Independent Forensic Verification**
Reconstruct preserved evidence later and compare the resulting cryptographic fingerprint against the trusted blockchain commitment.

**6. Structured Forensic Findings**
Classify verification outcomes according to the implemented forensic decision rules.

---

## System Architecture

```text
┌───────────────────────────────────────────────────────────┐
│                    IoT EDGE LAYER                         │
│ ESP32 • Sensors • FreeRTOS • Security Event Engine        │
└────────────────────────────┬──────────────────────────────┘
                             │ MQTT
                             ▼
┌───────────────────────────────────────────────────────────┐
│                 EVIDENCE INGESTION                         │
│ Node.js • TypeScript • Express • Zod                       │
│ RFC 8785 Canonicalization • SHA-256                        │
└────────────────────────────┬──────────────────────────────┘
                             ▼
┌───────────────────────────────────────────────────────────┐
│                 OFF-CHAIN PRESERVATION                     │
│ SQLite / Prisma • IPFS / Helia                             │
│ Complete Evidence Payload                                  │
└──────────────────────┬────────────────────────────────────┘
                       │ Evidence Commitment
                       ▼
┌───────────────────────────────────────────────────────────┐
│                  BLOCKCHAIN TRUST ANCHOR                   │
│ Ethereum / Hardhat • EvidenceRegistry.sol                  │
│ Compact Evidence Hash Commitment                           │
└────────────────────────────┬──────────────────────────────┘
                             │ Retrieve HASH_ANCHOR
                             ▼
┌───────────────────────────────────────────────────────────┐
│                  FORENSIC VERIFICATION                     │
│ Evidence Reconstruction • Re-hashing • Reconciliation      │
│ 7-Dimension Evaluation                                     │
└────────────────────────────┬──────────────────────────────┘
                             ▼
                  INTACT / ANOMALY / TAMPERED
```

---

## End-to-End Evidence Lifecycle

```text
01  EVENT GENERATION  →  02  VALIDATION  →  03  CANONICALIZATION
        ↓
04  CRYPTOGRAPHIC FINGERPRINTING  →  05  OFF-CHAIN PRESERVATION
        ↓
06  BLOCKCHAIN ANCHORING  →  07  FORENSIC RECONSTRUCTION
        ↓
08  HASH RECONCILIATION  →  09  FORENSIC FINDING
```

---

## Technology Stack

**IoT / Edge:** ESP32, FreeRTOS, DHT22, MQ-2, PIR, LDR, Physical tamper switch, Wokwi-based test environment

**Communication:** MQTT, QoS 1, Structured security-event topic

**Evidence Gateway:** Node.js, TypeScript, Express, Zod, RFC 8785 JSON Canonicalization Scheme, SHA-256

**Evidence Preservation:** SQLite, Prisma, IPFS, Helia

**Blockchain:** Ethereum-compatible EVM, Hardhat local blockchain, Solidity, `EvidenceRegistry.sol`, ethers.js, JSON-RPC

**Presentation:** HTML5, CSS3, JavaScript, Responsive presentation layout, Custom typography and design tokens

---

## IoT Edge Layer

| Input | Purpose |
|---|---|
| DHT22 | Temperature / humidity |
| MQ-2 | Gas / smoke |
| PIR | Motion detection |
| LDR | Light level |
| Tamper Switch | Enclosure state |

Example structured event:

```json
{
  "id": "EVT-00125",
  "dev": "ESP32-NODE-001",
  "seq": 125,
  "time": 1788912000,
  "type": "GAS_SPIKE",
  "gas_ppm": 712,
  "sev": "CRITICAL"
}
```

---

## Evidence Ingestion

```text
MQTT → Schema Validation → RFC 8785 Canonicalization → SHA-256 → Evidence Record
```

Zod is used as a runtime schema guard. Invalid input is rejected rather than silently accepted as evidence.

---

## Cryptographic Fingerprinting

```text
Semantically Equivalent JSON → RFC 8785 JCS → Canonical Bytes → SHA-256 → Evidence Digest
```

**Evidence Hash ≠ Transaction Hash ≠ Block Hash** — these three values serve different purposes and must not be conflated during forensic verification.

---

## Evidence Preservation

```text
Complete Evidence
      │
      ├── SQLite / Prisma  →  Structured metadata and retrieval context
      └── IPFS / Helia     →  Content-addressed evidence payload

OFF-CHAIN: Complete Evidence + Metadata
        ↓
ON-CHAIN: Compact Cryptographic Commitment
```

---

## Blockchain Evidence Anchoring

Smart contract: `EvidenceRegistry.sol`

```text
Preserved Evidence → SHA-256 Digest → Evidence Hash → EvidenceRegistry.sol → Blockchain State
```

Local development uses a Hardhat EVM testbed.

---

## Forensic Verification

```text
Preserved Evidence               Blockchain
        ↓                             ↓
   Reconstruct               EvidenceRegistry
        ↓                             ↓
RFC 8785 Canon.           Retrieve Commitment
        ↓                             ↓
     SHA-256                    HASH_ANCHOR
        ↓
   HASH_LOCAL  ↔  HASH_ANCHOR
```

### Seven-Dimension Forensic Evaluation

| # | Dimension |
|---|---|
| 01 | Schema Integrity |
| 02 | Device Identity |
| 03 | Sequence Integrity |
| 04 | Temporal Consistency |
| 05 | Payload Hash |
| 06 | IPFS CID Resolution |
| 07 | Blockchain Anchor |

---

## Forensic Verdict Model

**INTACT** — Evidence reconciles with trusted blockchain commitment; contextual checks clean.

**ANOMALY** — Operational or contextual deviation, but no cryptographic post-collection tampering established. Examples: replay attempt, sequence discontinuity, device identity anomaly, RPC unavailability.

**TAMPERED** — `HASH_LOCAL ≠ HASH_ANCHOR`

**UNANCHORED** — No external commitment exists. Not automatically tampered — independent reconciliation is unavailable.

> A blockchain or RPC failure must not automatically be interpreted as evidence tampering: `RPC Failure → ANOMALY`, not `TAMPERED`.

---

## Threat Scenarios

| # | Scenario | Finding | Result |
|---|---|---|---|
| 01 | Clean Evidence | INTACT | PASS |
| 02 | Database Modification | TAMPERED | PASS |
| 03 | Evidence Deletion | TAMPERED | PASS |
| 04 | Anchor Divergence | TAMPERED | PASS |
| 05 | Replay Attack | ANOMALY | PASS |
| 06 | Sequence Manipulation | ANOMALY | PASS |
| 07 | Device Spoofing | ANOMALY | PASS |
| 08 | Blockchain / RPC Failure | ANOMALY | PASS |
| 09 | Cross-Device Isolation | ISOLATED / ACCESS BLOCKED | PASS |

**Scenario distribution:** 9 executed — 1 INTACT · 3 TAMPERED · 4 ANOMALY · 1 ISOLATED

**Tampering Demonstration:** Simulated modification `712 ppm → 120 ppm` produces:

```text
HASH_LOCAL  0x91d2e7...4af1  ≠  HASH_ANCHOR  0xa8f913...c724  →  TAMPERED
```

The blockchain supplies the commitment. The forensic verifier performs reconciliation. The blockchain itself does not produce the verdict.

---

## Validation Results

| Suite | Result |
|---|---|
| Unit Tests | 89 / 89 PASS |
| Integration Tests | 25 / 25 PASS |
| Security & Isolation Audit | TASK #19 — PASS |
| Forensic Independence | INDEPENDENT — VALIDATED |

---

## Forensic Independence

The forensic engine does not treat the local tamper-audit log as the ultimate source of truth. It reconstructs evidence and reconciles the resulting cryptographic fingerprint with the external blockchain commitment — making the verification independent of the potentially compromised local system.

---

## Academic Contribution

| Discipline | Contribution |
|---|---|
| IoT Security | Generates structured security-relevant events |
| Digital Forensics | Preserves and reconstructs evidence |
| Blockchain | Provides an independent cryptographic commitment |

The architecture addresses the specific trust gap between a locally preserved evidence record and an independent historical reference.

---

## Presentation Structure

**Part 0 — Introduction & Problem Space:** ChainForensics, IoT evidence problem, conventional logging limitations, research gap, project motivation.

**Part 1 — Theoretical Foundations:** IoT, IoT Security, Blockchain Fundamentals, Blockchain as Trust Anchor, Digital Forensics, IoT Forensics, Evidence Integrity, theory-to-project bridge.

**Part 2 — Architecture, Implementation & Validation:** Architecture, IoT edge, evidence ingestion, canonicalization, fingerprinting, preservation, provenance, blockchain anchoring, forensic verification, verdict logic, threat scenarios, tampering demonstration, validation results.

**Part 3 — Conclusion & Future Roadmap:** Project conclusion, academic contributions, limitations, future work, research direction.

The current source contains **24 presentation slides**.

---

## Presentation Design System

| Token | Value |
|---|---|
| Primary Canvas | `#FFFFFF` |
| Dark Navy | `#182238` |
| Accent Orange | `#FF7A00` |
| Soft Surface | `#F8FAFC` |
| Success | `#059669` |

| Typeface | Role |
|---|---|
| Georgia | Primary presentation headings |
| Times New Roman | Academic body content |
| Courier New | Technical identifiers / code / hashes / system labels |

---

## Running the Presentation

**Option 1 — Direct Browser:** Open `index.html` in a modern web browser.

**Option 2 — Local HTTP Server:**

```bash
python -m http.server 8000
# then open http://localhost:8000
```

---

## Keyboard Controls

| Key | Action |
|---|---|
| `←` / `↑` | Previous slide |
| `→` / `↓` | Next slide |
| `Space` | Next slide |
| `F` | Toggle fullscreen |

---

## Repository Structure

```text
chainforensics-presentation/
│
├── index.html        # Presentation structure, slides, content, navigation
├── style.css         # Design tokens, typography, layout, colors, geometry
├── script.js         # Slide navigation, keyboard controls, fullscreen logic
│
├── assets/
│   ├── images/
│   └── screenshots/
│
├── README.md
└── LICENSE
```

---

## Research Scope and Limitations

1. **Controlled Testbed** — Validation is performed against the implemented project environment and defined scenarios.
2. **Sensor Environment** — The prototype uses a defined ESP32 sensor configuration rather than the full diversity of production IoT deployments.
3. **Blockchain Environment** — Validation uses a Hardhat local EVM test environment, not a production public blockchain.
4. **Attack Coverage** — The executed scenarios demonstrate implemented forensic behavior but cannot represent every possible real-world attack.
5. **Evidence Availability** — Blockchain anchoring provides a reference to a commitment. It does not automatically recover deleted off-chain evidence.

---

## Important Technical Distinctions

**Blockchain ≠ Forensic Engine** — Blockchain stores the commitment. Forensic engine performs verification.

**Evidence Hash ≠ Transaction Hash** — Evidence hash fingerprints evidence. Transaction hash identifies a blockchain transaction.

**Integrity ≠ Attribution** — A cryptographic mismatch demonstrates divergence from the trusted commitment. It does not identify who modified the record or the complete attack path.

**Anomaly ≠ Tampering** — `RPC Failure → ANOMALY`, not `TAMPERED`. `Replay Attempt → ANOMALY` unless preserved evidence demonstrates cryptographic divergence.

**Blockchain ≠ Complete Chain of Custody** — The blockchain acts as an independent cryptographic reference within the broader evidence provenance architecture.

---

## Future Work

1. **Distributed IoT Deployment** — Multiple IoT nodes, gateways, distributed evidence collectors, larger device fleets.
2. **Hardware-Backed Identity** — Secure elements, hardware-backed credentials, trusted execution mechanisms (ATECC608A, TPM).
3. **Scalable Evidence Infrastructure** — Evidence batching, Merkle-tree commitments, higher-throughput anchoring.
4. **Advanced Forensic Analytics** — Temporal correlation, behavioral analysis, cross-device correlation, incident graphs, automated anomaly analysis.

---

## Academic Positioning

The central academic proposition:

> A preserved IoT evidence record can be independently checked against an externally anchored cryptographic commitment, allowing the forensic verifier to detect divergence between the reconstructed evidence and the trusted reference.

### Core Architectural Principle

> IoT generates the event.  
> Digital forensics preserves and examines the evidence.  
> Blockchain provides the independent commitment.  
> The forensic verifier determines whether the reconstructed evidence still reconciles with that commitment.

---

## Project Status

| Component | Status |
|---|---|
| Presentation | 24 Slides |
| IoT Edge | Implemented |
| Evidence Ingestion | Implemented |
| Canonicalization | Implemented |
| SHA-256 Fingerprinting | Implemented |
| Off-Chain Preservation | Implemented |
| Blockchain Anchoring | Implemented |
| Forensic Verification | Implemented |
| Threat Scenarios | 9 Executed |
| Unit Tests | 89 / 89 PASS |
| Integration Tests | 25 / 25 PASS |
| Security / Isolation Audit | TASK #19 — PASS |
| Forensic Independence | VALIDATED |

---

## Acknowledgements

Developed as an academic B.Tech capstone project under:

**Woxsen University — School of Technology**

The project integrates concepts from IoT Security, Cybersecurity, Digital Forensics, Blockchain Technology, Cryptography, Distributed Systems, and Software Engineering.

---

## License

Add the project's selected license here. For academic/private use, replace this section with the appropriate institutional licensing statement.

---

*ChainForensics — From recorded IoT events to independently verifiable forensic evidence.*
