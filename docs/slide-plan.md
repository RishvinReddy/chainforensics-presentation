# ChainForensics Presentation Plan

> **Simple to look at, simple to explain, technically strong underneath.**

Your project itself is complex. **The PPT should not look complex.**

25 slides exactly, including the title and thank-you slides. This gives enough room for theory, literature review, project methodology, implementation, architecture, results, and conclusion without stuffing slides.

---

# 1. New Presentation Philosophy

### What we want

* Clean
* Professional
* Academic
* Humanised
* Easy to understand
* Easy to present
* Large readable text
* One main idea per slide
* Strong diagrams
* Minimal visual decoration
* Technical depth where it matters
* Clear connection between **IoT Security → Digital Forensics → Blockchain**
* Clear demonstration that this is an actual implemented project

### What we DON'T want

* Dashboard-like layouts
* Too many cards
* Too many pills/badges
* Too many tiny labels
* Huge paragraphs
* Over-engineered diagrams
* Excessive borders
* Excessive colours
* UI-style clutter
* 10 different things competing for attention
* Generic cybersecurity graphics
* Headers on every slide
* Footers on every slide
* Slide-number badges
* Decorative elements that don't communicate anything

---

# 2. Global Visual System

A **16:9 academic technical presentation**.

### Typography

| Element               | Font            | Approx. size |
| --------------------- | --------------- | -----------: |
| Main title            | Georgia         |     38–46 pt |
| Subtitle              | Times New Roman |     20–24 pt |
| Section title         | Georgia         |     34–40 pt |
| Body                  | Times New Roman |     18–22 pt |
| Diagram labels        | Times New Roman |     16–20 pt |
| Technical/code        | Courier New     |     15–18 pt |
| Small supporting text | Times New Roman |     15–17 pt |

No text should become microscopic just to fit a slide.

### Colours

Keep it restrained:

* Navy / dark blue → primary
* Orange → project accent
* White / warm off-white → background
* Light grey → secondary structures
* Green → verified / INTACT
* Amber → ANOMALY
* Red → TAMPERED

No rainbow palette.

---

# 3. NO HEADER / NO FOOTER

This is now **locked**.

Every slide should simply have:

```text
TITLE

MAIN VISUAL / CONTENT

Supporting explanation if required
```

No persistent:

* university header
* department header
* project badge
* section breadcrumb
* footer bar
* student names
* slide number
* decorative footer

The **title itself is enough**.

The title slide can contain university/project information naturally.

---

# 4. Complete 25-Slide Plan

Here is the structure.

---

## SLIDE 01 — TITLE

### **ChainForensics**

**Blockchain-Backed IoT Forensic Evidence Platform**

Supporting line:

**IoT Security × Digital Forensics × Blockchain**

University / department / team information can be placed naturally here.

### Visual

One clean central diagram:

```text
IoT Event
    ↓
Digital Evidence
    ↓
SHA-256
    ↓
Blockchain Anchor
    ↓
Forensic Verification
```

### Purpose

Establish the project immediately.

**Do not overload this slide.**

---

# PART A — INTRODUCTION

## SLIDE 02 — INTRODUCTION TO THE PRESENTATION

### Title

**Presentation Overview**

Simple five-part roadmap:

```text
01  Problem & Motivation
        ↓
02  Theory & Literature
        ↓
03  ChainForensics Design
        ↓
04  Implementation & Validation
        ↓
05  Results & Conclusion
```

### Purpose

Tell the faculty:

> "This is where we are going."

No complicated graphics.

---

## SLIDE 03 — PROBLEM STATEMENT

### Title

**The Problem: Can IoT Evidence Still Be Trusted After an Incident?**

Visual:

```text
IoT Device
    ↓
Security Event
    ↓
Local Log
    ↓
System Compromised
    ↓
Modify / Delete / Replay
    ↓
Can the original evidence still be verified?
```

Three simple problem points:

* Modification
* Deletion
* Replay / sequence manipulation

### Purpose

Make the problem understandable in **30 seconds**.

---

## SLIDE 04 — MOTIVATION & RESEARCH GAP

### Title

**Why Existing IoT Logging Is Not Enough**

Two-column comparison:

| Conventional approach | Missing capability                     |
| --------------------- | -------------------------------------- |
| Local database/logs   | Independent reference                  |
| Mutable records       | Post-collection integrity verification |
| Centralized trust     | External verification path             |
| Telemetry collection  | Forensic evidence preservation         |

Then one central statement:

> **The research gap is the absence of an independent mechanism for later verification of preserved IoT evidence.**

### Purpose

Clearly establish the academic motivation.

---

# PART B — THEORY

Only **4 theory slides**.

---

## SLIDE 05 — IoT FUNDAMENTALS

### Title

**Internet of Things**

Simple diagram:

```text
Physical Environment
        ↓
     Sensors
        ↓
    Edge Device
        ↓
   Communication
        ↓
     Application
```

Then map it lightly:

```text
Sensors → ESP32 → MQTT → Evidence Gateway
```

### Explain

* IoT connects physical devices to digital systems.
* Devices continuously generate telemetry.
* Security-relevant telemetry can become the starting point for forensic evidence.

---

## SLIDE 06 — IoT SECURITY

### Title

**IoT Security: Where Can an Attack Occur?**

One clean three-layer diagram:

```text
┌──────────────────────┐
│ DEVICE               │
│ ESP32 / Sensors      │
└──────────┬───────────┘
           ↓
┌──────────────────────┐
│ COMMUNICATION        │
│ MQTT / Network       │
└──────────┬───────────┘
           ↓
┌──────────────────────┐
│ DATA / BACKEND       │
│ Logs / Database      │
└──────────────────────┘
```

Beside it:

* Device spoofing
* Physical tampering
* Replay
* Sequence manipulation
* Data modification
* Evidence deletion

### Purpose

Connect IoT theory directly to your security problem.

---

## SLIDE 07 — BLOCKCHAIN FUNDAMENTALS

### Title

**Blockchain Fundamentals**

Only teach the concepts needed for your project:

```text
Transaction
     ↓
Hash
     ↓
Block
     ↓
Distributed Ledger
     ↓
Persistent State
```

Then:

**Smart Contract**

→ programmable blockchain logic.

### Purpose

Faculty should understand blockchain before seeing your smart contract.

Don't teach blockchain history.
Don't explain Bitcoin.
Don't spend half the presentation on consensus algorithms.

---

## SLIDE 08 — DIGITAL FORENSICS

### Title

**Digital Forensics**

Simple lifecycle:

```text
Identify
   ↓
Collect
   ↓
Preserve
   ↓
Examine
   ↓
Analyze
   ↓
Report
```

Highlight:

**PRESERVE**

Then three concepts:

* Integrity
* Provenance
* Chain of Custody

### Purpose

Explain why evidence preservation matters.

---

# PART C — LITERATURE REVIEW

## SLIDE 09 — LITERATURE REVIEW

### Title

**Literature Review**

Use a **simple academic comparison table**.

Recommended columns:

| Study / Approach | IoT | Blockchain | Forensics | Evidence Integrity | Limitation |
| ---------------- | --- | ---------- | --------- | ------------------ | ---------- |

Use your actual selected papers here.

Do **not** put full paper abstracts.

Each paper should be represented by:

* Author/year
* Main approach
* What it contributes
* What it does not solve

Approximately **5 papers** on this slide.

---

## SLIDE 10 — LITERATURE GAP

### Title

**What Is Missing in Existing Approaches?**

Instead of another huge table, use a simple matrix:

```text
                       IoT     Blockchain     Forensics
---------------------------------------------------------
IoT monitoring          ✓          —              —
Blockchain evidence    ✓          ✓              △
IoT forensics           ✓          —              ✓
Integrated verification ✓         ✓              ✓
```

Then highlight the gap:

### **Independent verification of IoT forensic evidence**

Bottom:

```text
IoT Security
     +
Digital Forensics
     +
Blockchain
     ↓
ChainForensics
```

### Purpose

This is where you establish the **research contribution**.

---

# PART D — PROJECT

## SLIDE 11 — PROJECT OBJECTIVES

### Title

**Project Objectives**

Only four objectives:

```text
01  CAPTURE
Generate structured security events from IoT devices.

02  PRESERVE
Create deterministic, integrity-protected evidence.

03  ANCHOR
Store a compact cryptographic commitment on blockchain.

04  VERIFY
Independently compare preserved evidence with the trusted reference.
```

Four large areas.

Very clean.

---

## SLIDE 12 — IMPLEMENTATION PLAN

### Title

**Implementation Plan**

Show the actual development sequence:

```text
1. IoT Event Generation
          ↓
2. MQTT Communication
          ↓
3. Evidence Ingestion
          ↓
4. Canonicalization & Hashing
          ↓
5. Off-Chain Preservation
          ↓
6. Blockchain Anchoring
          ↓
7. Forensic Verification
          ↓
8. Attack & Integrity Testing
```

### Purpose

Demonstrate that the project was systematically implemented.

---

## SLIDE 13 — PROJECT OVERVIEW

### Title

**ChainForensics: From IoT Event to Forensic Finding**

Main project overview diagram:

```text
┌─────────────┐
│ IoT Edge    │
│ ESP32       │
└──────┬──────┘
       │ MQTT
       ↓
┌─────────────┐
│ Evidence    │
│ Gateway     │
└──────┬──────┘
       │
       ↓
┌─────────────────────────┐
│ Evidence Preservation   │
│ SQLite + IPFS / Helia   │
└───────────┬─────────────┘
            │
       SHA-256
            ↓
┌─────────────────────────┐
│ Blockchain Anchor       │
│ EvidenceRegistry.sol    │
└───────────┬─────────────┘
            ↓
┌─────────────────────────┐
│ Forensic Verification   │
└───────────┬─────────────┘
            ↓
   INTACT / ANOMALY /
       TAMPERED
```

This is the **one diagram the faculty should remember**.

---

# PART E — IMPLEMENTATION

## SLIDE 14 — IoT EDGE IMPLEMENTATION

### Title

**IoT Edge Implementation**

Show the physical system simply:

```text
DHT22
MQ-2
PIR
LDR
Tamper Switch
      ↓
    ESP32
      ↓
Security Event Engine
      ↓
     MQTT
```

Mention existing implementation technologies:

* ESP32
* FreeRTOS
* Sensors
* Sequence tracking
* Event classification
* MQTT

Visual:

Wokwi circuit screenshot (as evidence of implementation).

---

## SLIDE 15 — SECURITY EVENT GENERATION

### Title

**From Sensor Telemetry to Security Event**

Show one example:

```text
Sensor Condition
      ↓
Threshold / Rule Evaluation
      ↓
Security Condition
      ↓
Structured Event
```

Example existing event:

```text
EVT-00125
ESP32-NODE-001
SEQ #125
MQ-2 = 712 ppm
SEVERITY = CRITICAL
```

Then:

```text
Telemetry ≠ Evidence

Security-relevant telemetry
              ↓
       Structured event
```

### Purpose

Explain the important transformation.

---

## SLIDE 16 — EVIDENCE PROCESSING

### Title

**Evidence Ingestion & Cryptographic Fingerprinting**

A very clean four-step diagram:

```text
MQTT Event
    ↓
Schema Validation
    ↓
RFC 8785 Canonicalization
    ↓
SHA-256
    ↓
Evidence Hash
```

Tiny visual example:

```text
{"a":1,"b":2}

        ↓ canonicalization

Deterministic representation

        ↓

SHA-256

        ↓

32-byte digest
```

Do not fill this slide with technical prose.

---

## SLIDE 17 — EVIDENCE PRESERVATION

### Title

**Evidence Preservation & Provenance**

Simple dual-storage architecture:

```text
             Evidence
                 │
       ┌─────────┴─────────┐
       ↓                   ↓
    SQLite              IPFS/Helia
   Metadata          Full Payload
       │                   │
       └─────────┬─────────┘
                 ↓
          Evidence Record
```

Provenance line:

```text
Generate → Preserve → Anchor → Verify
```

### Important

Explain:

> Blockchain is an independent anchor within the broader evidence-provenance process.

Not the entire chain of custody.

---

## SLIDE 18 — BLOCKCHAIN ANCHORING

### Title

**Blockchain Evidence Anchoring**

Simple:

```text
Evidence
   ↓
SHA-256
   ↓
32-byte evidenceHash
   ↓
EvidenceRegistry.sol
   ↓
Ethereum / Hardhat
```

Essential contract structure:

```text
EvidenceRecord

evidenceHash
timestamp
submitter
metadataCid
isRegistered
```

### Purpose

Explain exactly what goes on-chain.

Do not show the entire Solidity contract.

---

## SLIDE 19 — FORENSIC VERIFICATION

### Title

**How Is Evidence Verified Later?**

Two paths:

```text
LOCAL EVIDENCE                    TRUSTED REFERENCE

SQLite / IPFS                     Blockchain
      ↓                                ↓
Reconstruct payload              Read evidenceHash
      ↓                                ↓
RFC 8785                            Anchor Hash
      ↓                                ↓
SHA-256                               │
      ↓                                │
 HASH_LOCAL ─────────── COMPARE ──────┘
                         ↓
                      FINDING
```

This makes the core innovation immediately understandable.

---

## SLIDE 20 — FORENSIC VERDICT ENGINE

### Title

**From Verification to Forensic Finding**

Simple decision flow:

```text
Evidence Received
       ↓
Structural Check
       ↓
Contextual Check
       ↓
Blockchain Check
       ↓
Hash Reconciliation
       ↓
┌──────────┬───────────┬────────────┐
│  INTACT  │  ANOMALY  │  TAMPERED  │
└──────────┴───────────┴────────────┘
```

Explain very briefly:

* **INTACT**: Trusted reference and preserved evidence reconcile.
* **ANOMALY**: Contextual/sequence/operational inconsistency.
* **TAMPERED**: Cryptographic integrity divergence.

Keep it visually simple.

---

# PART F — VALIDATION / DEMONSTRATION

## SLIDE 21 — ATTACK SCENARIOS

### Title

**Threat Scenarios Tested**

Simple table:

| Scenario              | Expected finding |
| --------------------- | ---------------- |
| Clean evidence        | INTACT           |
| Replay                | ANOMALY          |
| Sequence manipulation | ANOMALY          |
| Device spoofing       | ANOMALY          |
| Database modification | TAMPERED         |
| Evidence deletion     | TAMPERED         |
| Blockchain mismatch   | TAMPERED         |
| RPC failure           | ANOMALY          |

No huge explanations. The presenter explains them verbally.

---

## SLIDE 22 — TAMPERING DEMONSTRATION

### Title

**Tampering Demonstration**

Before/after visual:

```text
BEFORE

Gas = 712 ppm
Hash = a8f913...c724
        ↓
Blockchain Anchor


        ATTACK

Gas changed:
712 ppm → 120 ppm


        ↓

AFTER

Recalculated Hash
91d2e7...4af1

        ≠

Trusted Anchor
a8f913...c724

        ↓

TAMPERED
```

This is your **hero experiment**.

Don't clutter it with unrelated information.

---

## SLIDE 23 — IMPLEMENTATION & RESULTS

### Title

**Implementation & Validation Results**

Three large result areas:

### Implementation

```text
ESP32
MQTT
Node.js / TypeScript
SQLite / Prisma
IPFS / Helia
Ethereum / Hardhat
Solidity
ethers.js
```

### Validation

```text
89 / 89
Unit Tests

25 / 25
Integration Tests

Task #19
Security Audit
PASS
```

### Forensic validation

Show key scenario outcomes. Keep it extremely readable.

---

# PART G — CONCLUSION

## SLIDE 24 — CONTRIBUTION, LIMITATIONS & FUTURE WORK

### Title

**Contribution & Future Direction**

Three contribution areas:

```text
IoT Security
Security-event generation
Device identity
Sequence tracking
Physical tamper detection
```

```text
Digital Forensics
Evidence preservation
Canonical representation
Integrity verification
Forensic evaluation
```

```text
Blockchain
Independent reference
EvidenceRegistry
Compact hash anchoring
External verification
```

Future-work strip:

```text
Trusted Hardware
        |
Scalable Anchoring
        |
Permissioned Blockchain
        |
Advanced Forensic Analytics
```

### Purpose

Answer:

> "What did your project contribute, and what comes next?"

---

## SLIDE 25 — THANK YOU

### **Thank You**

Keep this extremely simple.

Central:

```text
CHAINFORENSICS

Blockchain-Backed IoT Forensic Evidence Platform
```

Then:

**Questions & Discussion**

Optionally team/university information can appear here.

### Visual

One small, elegant project pipeline:

```text
IoT
 ↓
Evidence
 ↓
Blockchain
 ↓
Verification
```

That's it. **No huge infographic.**

---

# 5. Final Slide Distribution

|  # | Slide                      | Category       |
| -: | -------------------------- | -------------- |
|  1 | ChainForensics — Title     | Title          |
|  2 | Presentation Overview      | Introduction   |
|  3 | The Problem                | Introduction   |
|  4 | Motivation & Research Gap  | Introduction   |
|  5 | Internet of Things         | Theory         |
|  6 | IoT Security               | Theory         |
|  7 | Blockchain Fundamentals    | Theory         |
|  8 | Digital Forensics          | Theory         |
|  9 | Literature Review          | Literature     |
| 10 | Literature Gap             | Literature     |
| 11 | Project Objectives         | Project        |
| 12 | Implementation Plan        | Project        |
| 13 | ChainForensics Overview    | Project        |
| 14 | IoT Edge Implementation    | Implementation |
| 15 | Security Event Generation  | Implementation |
| 16 | Evidence Processing        | Implementation |
| 17 | Evidence Preservation      | Implementation |
| 18 | Blockchain Anchoring       | Implementation |
| 19 | Forensic Verification      | Implementation |
| 20 | Forensic Verdict Engine    | Implementation |
| 21 | Attack Scenarios           | Validation     |
| 22 | Tampering Demonstration    | Validation     |
| 23 | Implementation & Results   | Results        |
| 24 | Contribution & Future Work | Conclusion     |
| 25 | Thank You                  | Closing        |

---

# 6. The Most Important Change

Use **4–5 layout patterns** repeatedly:

* **Layout A — Concept slide** (Slides 5–8)
* **Layout B — Comparison slide** (Literature / Problem / Gap)
* **Layout C — Pipeline slide** (Implementation sequence)
* **Layout D — Architecture slide** (Architecture / Verification)
* **Layout E — Results slide** (Validation / Results)

---

# 7. What We Should Avoid This Time

* **No dashboard UI.**
* **No card for every sentence.**
* **No pill for every keyword.**
* **No tiny technical labels everywhere.**
* **No giant paragraphs.**
* **No excessive borders.**
* **No unnecessary gradients.**
* **No decorative cybersecurity graphics.**
* **No persistent header/footer.**
* **No slide-number badges.**
* **No complicated multi-layer diagrams unless the slide specifically needs one.**
* **No putting the entire architecture on every project slide.**

> **One slide = one idea. One idea = one dominant visual.**

---

# 8. The Story of the New Presentation

```text
WHY?
 ↓
IoT evidence can be changed after an incident.
 ↓
WHAT IS NEEDED?
 ↓
An independent way to verify preserved evidence.
 ↓
WHAT DOES THEORY GIVE US?
 ↓
IoT + Blockchain + Digital Forensics
 ↓
WHAT DID WE BUILD?
 ↓
ChainForensics
 ↓
HOW?
 ↓
Capture → Preserve → Hash → Anchor → Verify
 ↓
DOES IT WORK?
 ↓
Attack scenarios + Tampering demonstration + Tests
 ↓
WHAT DID WE CONTRIBUTE?
 ↓
Independent verification of IoT forensic evidence
```
