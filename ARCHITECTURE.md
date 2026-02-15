# 🏗️ Master Architecture: AI-Native Education Ecosystem

> **Version:** 2.0 &nbsp;|&nbsp; **Last Updated:** February 15, 2026  
> **Status:** Living Document — Evolves with each deployment phase

A unified technical and pedagogical blueprint for a **modular, data-driven learning platform** that integrates **MCP (Model Context Protocol)**, **Gemini 3 Pro** reasoning, and a **Mastery-based evaluation framework** to deliver deeply personalized education at scale across India.

---

## Table of Contents

1. [System Philosophy](#1-system-philosophy)
2. [High-Level System Overview](#2-high-level-system-overview)
3. [Technical Architecture — The MCP-Native Core](#3-technical-architecture--the-mcp-native-core)
4. [The "AI Factory" — Course Development Pipeline](#4-the-ai-factory--course-development-pipeline)
5. [Mastery Tree & Knowledge Graph](#5-mastery-tree--knowledge-graph)
6. [Evaluation & Testing Strategy](#6-evaluation--testing-strategy)
7. [Classroom Integration — Physical-Digital Bridge](#7-classroom-integration--physical-digital-bridge)
8. [Security, Privacy & Compliance](#8-security-privacy--compliance)
9. [Scalability & Infrastructure](#9-scalability--infrastructure)
10. [Deployment Roadmap](#10-deployment-roadmap)
11. [Key Design Decisions & Trade-offs](#11-key-design-decisions--trade-offs)
12. [Glossary](#12-glossary)

---

## 1. System Philosophy

The platform is built on four foundational pillars:

| Pillar | Principle | Implication |
|--------|-----------|-------------|
| **Schema-Driven** | Logic is defined by data structures and tool schemas, not hard-coded paths | New capabilities are added by registering new MCP tools — zero redeployment of the core |
| **Agentic Orchestration** | AI agents discover capabilities (tools) via MCP to fulfill student needs dynamically | The system self-assembles its workflow per student request |
| **Mastery-First** | Proficiency is measured through conceptual depth and transferability, not just completion | A student "passes" only when they can apply knowledge to novel, unseen contexts |
| **Equity by Design** | Every architectural choice accounts for low-bandwidth, multilingual, offline-first environments | India's Tier-2/3 cities and rural schools are first-class deployment targets |

```mermaid
mindmap
  root((AI-Native Education Ecosystem))
    Schema-Driven
      Tool Schemas define logic
      Zero-redeployment extensibility
      JSON-first contracts
    Agentic Orchestration
      MCP discovery protocol
      Dynamic workflow assembly
      Multi-agent collaboration
    Mastery-First
      Conceptual depth over completion
      Transfer tasks validate understanding
      Dependency-aware progression
    Equity by Design
      Offline-first architecture
      Regional language support
      Low-bandwidth optimization
```

---

## 2. High-Level System Overview

The following diagram captures the end-to-end flow from student interaction through AI processing to classroom feedback.

```mermaid
graph TB
    subgraph "👨‍🎓 Student Layer"
        A[Student — Mobile / Tablet / Paper]
        B[Teacher Dashboard]
    end

    subgraph "🌐 Edge Layer — School"
        C[Astra Hub — Edge MCP Server]
        D[Local Print Queue]
        E[Offline Data Store]
    end

    subgraph "🧠 Intelligence Layer — Cloud"
        F[AI Host — FastAPI + LangGraph]
        G[Gemini 3 Pro — Reasoning Engine]
        H[MCP Router]
    end

    subgraph "🔧 MCP Server Fleet"
        I[Moodle Bridge Server]
        J[Assessment & Vision Server]
        K[Content & Textbook Server]
        L[Localization Server]
    end

    subgraph "💾 Data Layer"
        M[(Headless Moodle — LMS)]
        N[(Knowledge Graph DB — Neo4j)]
        O[(Content Store — S3/MinIO)]
        P[(Analytics — ClickHouse)]
    end

    A -->|Submits work| C
    A -->|Online interaction| F
    B -->|Views heatmaps| F
    C -->|Syncs when online| F
    C --> D
    C --> E
    F <-->|Reasons| G
    F --> H
    H --> I
    H --> J
    H --> K
    H --> L
    I <--> M
    J <--> M
    K <--> O
    L <--> O
    F --> N
    F --> P

    style F fill:#4A90D9,stroke:#2C5F8A,color:#fff
    style G fill:#E8A838,stroke:#B8862D,color:#fff
    style C fill:#50C878,stroke:#3A9D5C,color:#fff
    style M fill:#9B59B6,stroke:#7D3C98,color:#fff
```

---

## 3. Technical Architecture — The MCP-Native Core

### 3A. The "Nervous System" — Orchestration Layer

The orchestration layer is the brain of the platform. It routes student needs to the right tools without any hard-coded logic.

| Component | Technology | Role |
|-----------|------------|------|
| **AI Host** | FastAPI + LangGraph | Central reasoning node — receives requests, plans multi-step actions, calls MCP tools |
| **Reasoning Engine** | Gemini 3 Pro | Provides deep pedagogical reasoning, content analysis, and evaluation |
| **MCP Protocol** | JSON-RPC 2.0 over stdio/SSE | Replaces traditional REST APIs — the Host *discovers* tool capabilities at runtime |
| **LMS Backend** | Headless Moodle | The "State of Truth" — single source for enrollment, grades, progress |
| **Knowledge Graph** | Neo4j | Stores the Mastery Tree, concept dependencies, and student traversal paths |
| **Analytics Engine** | ClickHouse | Real-time aggregation of engagement metrics, time-to-mastery, and cohort comparisons |

```mermaid
sequenceDiagram
    participant S as Student
    participant H as AI Host (LangGraph)
    participant G as Gemini 3 Pro
    participant R as MCP Router
    participant MB as Moodle Bridge
    participant AV as Assessment Server
    participant CT as Content Server

    S->>H: "I solved this physics problem" (image upload)
    H->>R: discover_tools()
    R-->>H: Available tools manifest
    H->>G: Plan evaluation strategy
    G-->>H: Step plan: [OCR → Evaluate Logic → Update Mastery → Generate Next Task]

    H->>AV: evaluate_handwriting(image)
    AV-->>H: {extracted_text, detected_steps, confidence}

    H->>G: Analyze solution steps for conceptual mastery
    G-->>H: {mastery_assessment, gaps: ["vector_decomposition"], score: 0.72}

    H->>MB: update_mastery_node(student_id, "vector_decomposition", 0.72)
    MB-->>H: ✅ Updated

    H->>CT: fetch_remedial_content("vector_decomposition", difficulty=0.6)
    CT-->>H: {content_block, exercises}

    H->>S: "Great work on Newton's 3rd Law! Let's strengthen vector decomposition — try this..."
```

### 3B. Modular MCP Server Fleet

Each MCP server is an independently deployable microservice exposing tools via the MCP protocol.

```mermaid
graph LR
    subgraph "MCP Server Fleet"
        direction TB

        subgraph "📚 Moodle Bridge Server"
            M1[get_student_profile]
            M2[update_mastery_node]
            M3[fetch_curriculum]
            M4[enroll_student]
            M5[get_cohort_analytics]
        end

        subgraph "🔬 Assessment & Vision Server"
            A1[evaluate_handwriting]
            A2[analyze_oral_explanation]
            A3[generate_transfer_task]
            A4[grade_diagram_accuracy]
            A5[detect_misconception]
        end

        subgraph "📖 Content & Textbook Server"
            C1["resource://textbook/{subject}/{chapter}"]
            C2[search_concept]
            C3[get_worked_example]
            C4[generate_simulation_params]
            C5[fetch_remedial_content]
        end

        subgraph "🌍 Localization Server"
            L1[translate_content]
            L2[culturally_adapt]
            L3[generate_regional_examples]
            L4[transliterate_formula]
        end

        subgraph "🏫 Astra Hub — Edge MCP"
            E1[trigger_local_print]
            E2[sync_offline_data]
            E3[cache_lesson_pack]
            E4[report_device_health]
            E5[queue_assessment_upload]
        end
    end
```

#### MCP Tool Schema Example

Every tool is defined by a strict JSON schema contract. This is what the AI Host sees when it discovers the Assessment Server:

```json
{
  "name": "evaluate_handwriting",
  "description": "OCR + logical analysis of a student's handwritten solution",
  "inputSchema": {
    "type": "object",
    "properties": {
      "image_base64": { "type": "string", "description": "Base64-encoded image of handwritten work" },
      "subject": { "type": "string", "enum": ["math", "physics", "chemistry", "biology"] },
      "expected_topic": { "type": "string", "description": "The concept the student was working on" },
      "student_id": { "type": "string" },
      "grading_rubric": {
        "type": "object",
        "properties": {
          "check_units": { "type": "boolean", "default": true },
          "check_diagram": { "type": "boolean", "default": false },
          "partial_credit": { "type": "boolean", "default": true }
        }
      }
    },
    "required": ["image_base64", "subject", "expected_topic", "student_id"]
  }
}
```

### 3C. Data Flow Architecture

```mermaid
flowchart LR
    subgraph Ingestion
        RAW[Raw Textbooks — PDF/EPUB]
        SCAN[Student Scans — Images]
        VOICE[Oral Explanations — Audio]
        INTERACT[Platform Interactions — Events]
    end

    subgraph Processing
        OCR[OCR Pipeline]
        ASR[Speech-to-Text — Whisper]
        NLP[Concept Extraction — Gemini]
        PARSER[Textbook Parser]
    end

    subgraph Storage
        MOODLE[(Moodle — Student State)]
        NEO4J[(Neo4j — Knowledge Graph)]
        S3[(MinIO — Media Assets)]
        CLICK[(ClickHouse — Analytics)]
    end

    subgraph Serving
        API[AI Host API]
        DASH[Teacher Dashboard]
        MOBILE[Student App]
        EDGE[Astra Hub]
    end

    RAW --> PARSER --> S3
    PARSER --> NEO4J
    SCAN --> OCR --> NLP --> MOODLE
    VOICE --> ASR --> NLP
    INTERACT --> CLICK

    MOODLE --> API
    NEO4J --> API
    S3 --> API
    CLICK --> DASH

    API --> MOBILE
    API --> EDGE
    API --> DASH
```

---

## 4. The "AI Factory" — Course Development Pipeline

The system scales content creation using an agentic pipeline that transforms raw textbooks into interactive, mastery-aligned learning journeys.

```mermaid
graph TD
    INPUT[📕 Raw Textbook — NCERT PDF] --> ARCH

    subgraph "AI Factory Pipeline"
        ARCH["🏛️ Architect Agent<br/>Parses textbook into Mastery Tree<br/>(Dependency Graph)"]
        SCRIBE["✍️ Scribe Agent<br/>Generates multimodal content<br/>(Scripts, Simulations, Exercises)"]
        LOCAL["🌐 Localization Agent<br/>Translates & culturally adapts<br/>into Indian regional languages"]
        CRITIC["🔍 Pedagogical Critic<br/>Audits for factual accuracy<br/>& instructional quality"]
        SYNTH["🤖 Synthetic Tester<br/>1000+ AI student personas<br/>simulate the course"]
    end

    ARCH --> SCRIBE --> LOCAL --> CRITIC --> SYNTH

    SYNTH -->|Issues found| CRITIC
    CRITIC -->|Revisions needed| SCRIBE
    SYNTH -->|✅ Approved| PUBLISH[📦 Published Course Module]

    style ARCH fill:#3498DB,stroke:#2471A3,color:#fff
    style SCRIBE fill:#2ECC71,stroke:#27AE60,color:#fff
    style LOCAL fill:#E67E22,stroke:#D35400,color:#fff
    style CRITIC fill:#E74C3C,stroke:#C0392B,color:#fff
    style SYNTH fill:#9B59B6,stroke:#8E44AD,color:#fff
    style PUBLISH fill:#1ABC9C,stroke:#16A085,color:#fff
```

### Agent Specifications

| Agent | Input | Output | Key Capabilities |
|-------|-------|--------|-------------------|
| **Architect** | Raw textbook PDF/EPUB | Mastery Tree JSON (DAG) | Chapter segmentation, concept extraction, prerequisite mapping, Bloom's taxonomy tagging |
| **Scribe** | Mastery Tree + Concept Nodes | Multimodal content packages | Video scripts, interactive simulations (PhET-style), scaffolded exercises, worked examples |
| **Localization** | English content packages | Regionalized content | Translation (Hindi, Tamil, Telugu, Bengali, Marathi, etc.), culturally relevant examples, local unit conversions |
| **Pedagogical Critic** | Generated content | Audit reports + revision directives | Factual verification against source textbook, cognitive load analysis, prerequisite alignment check |
| **Synthetic Tester** | Published course draft | Test reports + edge cases | Simulates 1000+ student personas across skill spectrums, detects hallucinations, dead-ends, unfair difficulty spikes |

### Content Generation Workflow — Detailed

```mermaid
stateDiagram-v2
    [*] --> TextbookIngestion
    TextbookIngestion --> ConceptExtraction: Parse chapters
    ConceptExtraction --> DependencyMapping: Identify prerequisites
    DependencyMapping --> MasteryTreeGeneration: Build DAG

    MasteryTreeGeneration --> ContentGeneration: For each node

    state ContentGeneration {
        [*] --> VideoScript
        [*] --> InteractiveSimulation
        [*] --> ExerciseSet
        [*] --> WorkedExamples
        VideoScript --> [*]
        InteractiveSimulation --> [*]
        ExerciseSet --> [*]
        WorkedExamples --> [*]
    }

    ContentGeneration --> Localization: Translate & adapt
    Localization --> QualityAudit: Critic reviews
    QualityAudit --> ContentGeneration: ❌ Revisions needed
    QualityAudit --> SyntheticTesting: ✅ Passes audit
    SyntheticTesting --> QualityAudit: ⚠️ Issues detected
    SyntheticTesting --> Published: ✅ All checks pass
    Published --> [*]
```

---

## 5. Mastery Tree & Knowledge Graph

The Mastery Tree is the structural backbone of personalized learning. It models **what** a student knows and **what they need next**.

### Concept Dependency Graph — Example (Physics: Mechanics)

```mermaid
graph TD
    UNITS["📐 Units & Measurements"] --> VECTORS["↗️ Vectors"]
    UNITS --> KINEMATICS["🏃 Kinematics"]
    VECTORS --> KINEMATICS
    KINEMATICS --> NEWTON["⚖️ Newton's Laws"]
    VECTORS --> NEWTON
    NEWTON --> FRICTION["🧱 Friction"]
    NEWTON --> CIRCULAR["🔄 Circular Motion"]
    NEWTON --> WORK["⚡ Work, Energy & Power"]
    KINEMATICS --> PROJECTILE["🎯 Projectile Motion"]
    VECTORS --> PROJECTILE
    CIRCULAR --> GRAVITATION["🌍 Gravitation"]
    WORK --> GRAVITATION
    WORK --> COLLISIONS["💥 Collisions & Momentum"]
    NEWTON --> COLLISIONS
    GRAVITATION --> SATELLITES["🛰️ Satellite Motion"]
    CIRCULAR --> SATELLITES

    classDef mastered fill:#2ECC71,stroke:#27AE60,color:#fff
    classDef inProgress fill:#F39C12,stroke:#E67E22,color:#fff
    classDef locked fill:#BDC3C7,stroke:#95A5A6,color:#555

    class UNITS,VECTORS,KINEMATICS mastered
    class NEWTON,PROJECTILE inProgress
    class FRICTION,CIRCULAR,WORK,GRAVITATION,COLLISIONS,SATELLITES locked
```

### Student State Model (per Mastery Node)

```json
{
  "student_id": "STU-2026-04521",
  "concept_id": "physics.mechanics.newtons_laws",
  "mastery_level": 0.72,
  "bloom_level": "application",
  "attempts": 5,
  "last_assessment": "2026-02-14T10:30:00Z",
  "misconceptions_detected": ["action_reaction_same_body", "force_implies_motion"],
  "transfer_tasks_passed": 1,
  "transfer_tasks_total": 3,
  "recommended_next": ["friction", "circular_motion"],
  "time_spent_minutes": 145
}
```

### Knowledge Graph Schema

```mermaid
erDiagram
    STUDENT ||--o{ MASTERY_NODE : "has progress on"
    MASTERY_NODE }o--|| CONCEPT : "tracks mastery of"
    CONCEPT ||--o{ CONCEPT : "depends on"
    CONCEPT ||--o{ CONTENT_BLOCK : "taught by"
    CONCEPT ||--o{ ASSESSMENT : "evaluated by"
    CONTENT_BLOCK ||--o{ LOCALIZED_VARIANT : "available in"
    STUDENT ||--o{ MISCONCEPTION : "has"
    MISCONCEPTION }o--|| CONCEPT : "related to"
    ASSESSMENT ||--o{ RUBRIC : "scored by"

    STUDENT {
        string student_id PK
        string name
        string school_id
        string grade
        string preferred_language
        json learning_style_profile
    }

    CONCEPT {
        string concept_id PK
        string subject
        string chapter
        string bloom_level
        float difficulty
        string[] prerequisites
    }

    MASTERY_NODE {
        string id PK
        float mastery_level
        int attempts
        datetime last_assessed
        string[] misconceptions
    }

    CONTENT_BLOCK {
        string block_id PK
        string type
        string media_url
        float difficulty
        int estimated_minutes
    }

    ASSESSMENT {
        string assessment_id PK
        string type
        json rubric
        float max_score
    }
```

---

## 6. Evaluation & Testing Strategy

### I. Student "Deep Understanding" Evaluation

Traditional MCQ-based testing is insufficient. This platform evaluates **conceptual depth** across three dimensions:

```mermaid
graph TD
    subgraph "🎯 Three Dimensions of Deep Understanding"
        CA["🔗 Conceptual Anchors<br/><i>Can the student articulate<br/>the core principle?</i>"]
        CT["🔀 Context Transfer<br/><i>Can they apply it<br/>to a novel scenario?</i>"]
        LT["📊 Logic Traceability<br/><i>Is their reasoning process<br/>sound and complete?</i>"]
    end

    INPUT[Student Submission<br/>Written / Oral / Digital] --> CA
    INPUT --> CT
    INPUT --> LT

    CA --> EVAL["🧠 Gemini 3 Pro<br/>Holistic Evaluation"]
    CT --> EVAL
    LT --> EVAL

    EVAL --> MASTERY[Mastery Score Update]
    EVAL --> FEEDBACK[Personalized Feedback]
    EVAL --> NEXT[Next Learning Path]

    style CA fill:#3498DB,stroke:#2471A3,color:#fff
    style CT fill:#E67E22,stroke:#D35400,color:#fff
    style LT fill:#2ECC71,stroke:#27AE60,color:#fff
    style EVAL fill:#9B59B6,stroke:#8E44AD,color:#fff
```

| Dimension | Method | Example |
|-----------|--------|---------|
| **Conceptual Anchors** | Gemini analyzes oral/written input for core principles, not keywords | Student explains *why* a ball slows down, not just "friction" |
| **Context Transfer** | Apply concepts to novel, real-world scenarios | "How does Newton's 3rd Law apply in a cricket bat hitting a ball?" |
| **Logic Traceability** | Grading focuses on process steps, identifying sub-concept gaps | In a multi-step math problem, pinpoints *where* the reasoning breaks |

### II. Platform Meta-Testing

```mermaid
graph LR
    subgraph "Shadow Mode — Observer Agents"
        OBS[Observer Agent] --> TTM[Time-to-Mastery Tracking]
        OBS --> ENGAGE[Engagement Dip Detection]
        OBS --> DROP[Drop-off Point Analysis]
        TTM --> FLAG[🚩 Flag Content for Refinement]
        ENGAGE --> FLAG
        DROP --> FLAG
    end

    subgraph "A/B Testing Engine"
        COHORT_A[Cohort A — Visual-First Pedagogy]
        COHORT_B[Cohort B — Problem-First Pedagogy]
        COHORT_C[Cohort C — Narrative-First Pedagogy]
        COHORT_A --> COMPARE[Statistical Comparison<br/>Effect Size + Significance]
        COHORT_B --> COMPARE
        COHORT_C --> COMPARE
        COMPARE --> WINNER[🏆 Optimal Instructional Path]
    end
```

### III. System Reliability — Synthetic Testing

```mermaid
flowchart TD
    GEN[Generate 1000+ Synthetic Student Personas] --> PROFILES

    subgraph PROFILES["Persona Spectrum"]
        P1["🌟 High Achiever<br/>Fast learner, few errors"]
        P2["📚 Average Student<br/>Steady pace, common misconceptions"]
        P3["🆘 Struggling Learner<br/>Frequent gaps, needs scaffolding"]
        P4["🌐 Non-Native Speaker<br/>Language barriers, regional context"]
        P5["♿ Accessibility Needs<br/>Screen reader, motor challenges"]
    end

    PROFILES --> SIM["Simulate Full Course Journey"]
    SIM --> CHECK

    subgraph CHECK["Validation Checks"]
        V1["🔍 Hallucination Detection"]
        V2["🚫 Dead-End Detection"]
        V3["📈 Difficulty Spike Analysis"]
        V4["📋 Schema Contract Validation"]
        V5["⏱️ Latency & Timeout Testing"]
    end

    CHECK -->|Issues Found| FIX[Auto-File Bug Reports]
    CHECK -->|✅ All Pass| CERTIFY[📜 Course Certified for Deployment]
```

---

## 7. Classroom Integration — Physical-Digital Bridge

The platform bridges the physical classroom and digital systems seamlessly.

```mermaid
sequenceDiagram
    participant T as 👩‍🏫 Teacher
    participant S as 👨‍🎓 Students (30)
    participant AH as 🏫 Astra Hub (Edge)
    participant AI as 🧠 AI Host (Cloud)
    participant M as 💾 Moodle

    Note over T,S: 📖 Classroom Session — Physics: Newton's Laws

    T->>S: Teaches concept + assigns worksheet
    S->>S: Solve problems on physical paper
    S->>AH: Submit scanned worksheets (camera/scanner)

    AH->>AH: Local OCR preprocessing
    AH->>AI: Upload processed scans (batch)

    AI->>AI: evaluate_handwriting() for each student
    AI->>AI: Gemini analyzes solution steps
    AI->>M: Update mastery_node for each student

    AI->>T: 📊 Comprehension Heatmap
    Note over T: "12 students struggle with<br/>vector decomposition in Q3"

    T->>AI: Request remedial content for vector decomposition
    AI->>AH: Send personalized worksheets

    AH->>AH: trigger_local_print()
    AH->>S: 🖨️ Custom remedial worksheet per student

    Note over S: Students work on targeted<br/>remediation — no one left behind
```

### Comprehension Heatmap — Teacher View

| Concept | Class Avg | Below Threshold | Action |
|---------|-----------|-----------------|--------|
| Newton's 1st Law | 0.85 ✅ | 3 students | Individual follow-up |
| Newton's 2nd Law (F=ma) | 0.78 ⚠️ | 7 students | Small group session |
| Vector Decomposition | 0.52 🔴 | 12 students | Full class re-teach + remedial prints |
| Free Body Diagrams | 0.68 ⚠️ | 9 students | Interactive simulation assignment |

### Offline-First Architecture — Astra Hub

```mermaid
flowchart TD
    subgraph "Astra Hub — Edge Server (School)"
        CACHE["📦 Cached Lesson Packs<br/>(Pre-synced content)"]
        LOCAL_AI["🤖 Lightweight Local Model<br/>(Basic evaluation only)"]
        QUEUE["📋 Assessment Queue<br/>(Pending cloud sync)"]
        PRINTER["🖨️ Local Printer"]
        HEALTH["❤️ Device Health Monitor"]
    end

    subgraph "Cloud"
        CLOUD_AI["🧠 AI Host"]
        CLOUD_STORE["💾 Central Store"]
    end

    CACHE --> LOCAL_AI
    LOCAL_AI --> QUEUE
    QUEUE -->|"When online"| CLOUD_AI
    CLOUD_AI -->|"Sync updates"| CACHE
    CLOUD_STORE -->|"Nightly sync"| CACHE
    LOCAL_AI --> PRINTER

    HEALTH -->|"Status reports"| CLOUD_AI
```

---

## 8. Security, Privacy & Compliance

### Data Protection Framework

| Layer | Measure | Details |
|-------|---------|---------|
| **Student Data** | End-to-end encryption | AES-256 at rest, TLS 1.3 in transit |
| **PII Handling** | DPDPA 2023 compliant | India's Digital Personal Data Protection Act — consent-based data collection |
| **Biometric Data** | Minimization principle | Handwriting/voice processed for evaluation only; raw data purged after analysis |
| **Access Control** | RBAC + ABAC | Role-based (teacher, student, admin) + Attribute-based (school, grade, region) |
| **Audit Trail** | Immutable logs | Every AI decision logged with reasoning chain for explainability |
| **Edge Security** | Hardware attestation | Astra Hubs use TPM-based device identity |

```mermaid
graph TD
    subgraph "Trust Boundary — School"
        STUDENT[Student Device] -->|TLS 1.3| ASTRA[Astra Hub]
        ASTRA -->|Encrypted Queue| GATEWAY[API Gateway]
    end

    subgraph "Trust Boundary — Cloud"
        GATEWAY -->|mTLS| AUTH[Auth Service — Keycloak]
        AUTH -->|JWT| HOST[AI Host]
        HOST -->|Scoped Tokens| MCP[MCP Servers]
        MCP -->|Encrypted| DB[(Encrypted Storage)]
    end

    subgraph "Audit & Compliance"
        HOST --> AUDIT[Audit Log — Immutable]
        MCP --> AUDIT
        AUDIT --> COMPLIANCE[Compliance Dashboard]
    end

    style AUTH fill:#E74C3C,stroke:#C0392B,color:#fff
    style AUDIT fill:#F39C12,stroke:#E67E22,color:#fff
```

---

## 9. Scalability & Infrastructure

### Deployment Topology

```mermaid
graph TB
    subgraph "CDN — CloudFront / Fastly"
        CDN[Static Assets + Cached Content]
    end

    subgraph "Load Balancer — Nginx / Envoy"
        LB[L7 Load Balancer]
    end

    subgraph "Compute — Kubernetes Cluster"
        subgraph "AI Host Pods (Auto-scaled)"
            HOST1[AI Host — Instance 1]
            HOST2[AI Host — Instance 2]
            HOSTN[AI Host — Instance N]
        end
        subgraph "MCP Server Pods"
            MCP1[Moodle Bridge × 3]
            MCP2[Assessment Server × 5]
            MCP3[Content Server × 3]
            MCP4[Localization Server × 2]
        end
    end

    subgraph "Data Tier"
        MOODLE_DB[(Moodle — PostgreSQL)]
        NEO4J_DB[(Neo4j Cluster)]
        MINIO[(MinIO — Object Storage)]
        CLICK_DB[(ClickHouse — Analytics)]
        REDIS[(Redis — Session + Cache)]
    end

    subgraph "Edge — 500+ Schools"
        ASTRA1[Astra Hub — School 1]
        ASTRA2[Astra Hub — School 2]
        ASTRAN[Astra Hub — School N]
    end

    CDN --> LB
    LB --> HOST1
    LB --> HOST2
    LB --> HOSTN
    HOST1 --> MCP1
    HOST1 --> MCP2
    HOST2 --> MCP3
    HOSTN --> MCP4
    MCP1 --> MOODLE_DB
    MCP2 --> MOODLE_DB
    MCP3 --> MINIO
    MCP4 --> MINIO
    HOST1 --> NEO4J_DB
    HOST2 --> REDIS
    HOSTN --> CLICK_DB

    ASTRA1 -->|Sync| LB
    ASTRA2 -->|Sync| LB
    ASTRAN -->|Sync| LB
```

### Performance Targets

| Metric | Target | Measurement |
|--------|--------|-------------|
| **API Latency (p95)** | < 200ms | AI Host response to MCP tool call |
| **Evaluation Turnaround** | < 30 seconds | From scan upload to mastery update |
| **Concurrent Students** | 50,000+ | Per region, auto-scaled |
| **Offline Autonomy** | 72 hours | Astra Hub operates without cloud connectivity |
| **Sync Recovery** | < 5 minutes | Full state sync after connectivity restored |
| **Content Generation** | 1 chapter/hour | AI Factory pipeline throughput |

---

## 10. Deployment Roadmap

```mermaid
gantt
    title AI-Native Education Platform — Deployment Roadmap
    dateFormat YYYY-MM
    axisFormat %b %Y

    section Phase 1 — Foundation
    Headless Moodle Setup           :done, p1a, 2026-02, 2026-03
    MCP Host + Gemini 3 Pro         :done, p1b, 2026-02, 2026-04
    Core MCP Servers (Moodle Bridge):active, p1c, 2026-03, 2026-05
    Knowledge Graph (Neo4j)         :p1d, 2026-04, 2026-06

    section Phase 2 — AI Factory
    Textbook Parser (NCERT Science) :p2a, 2026-05, 2026-07
    Mastery Tree Generation         :p2b, 2026-06, 2026-08
    Content Generation Pipeline     :p2c, 2026-07, 2026-09
    Textbook Parser (NCERT Math)    :p2d, 2026-07, 2026-09

    section Phase 3 — Pilot
    Assessment & Vision Server      :p3a, 2026-08, 2026-10
    Astra Hub (Edge) — 10 Schools   :p3b, 2026-09, 2026-11
    Vision Grading Pilot            :p3c, 2026-10, 2026-12
    Teacher Dashboard v1            :p3d, 2026-09, 2026-11

    section Phase 4 — Scale
    Regional Languages (5 languages):p4a, 2026-11, 2027-02
    500 School Rollout              :p4b, 2027-01, 2027-04
    JEE/NEET Exam Modules           :p4c, 2027-02, 2027-05
    Synthetic Testing at Scale      :p4d, 2027-01, 2027-03

    section Phase 5 — Maturity
    Full Autonomy Mode              :p5a, 2027-04, 2027-07
    International Expansion Prep    :p5b, 2027-05, 2027-08
    Open Source Community Edition   :p5c, 2027-06, 2027-09
```

### Phase Details

| Phase | Focus | Key Deliverables | Success Criteria |
|-------|-------|------------------|------------------|
| **Phase 1** | Foundation | Headless Moodle, MCP Host, Gemini integration, Neo4j | AI Host can discover and call MCP tools; student data flows end-to-end |
| **Phase 2** | AI Factory | NCERT Science & Math ingested into Mastery Trees | 100+ concept nodes with dependencies; content generated for each |
| **Phase 3** | Pilot | Vision grading, Astra Hub in 10 schools, Teacher Dashboard | 500+ students evaluated via scan; teachers report actionable heatmaps |
| **Phase 4** | Scale | 5 regional languages, 500 schools, JEE/NEET modules | <30s evaluation turnaround at scale; exam-readiness metrics correlate with results |
| **Phase 5** | Maturity | Full autonomy, international prep, open-source edition | Platform self-improves via shadow mode; community contributions active |

---

## 11. Key Design Decisions & Trade-offs

| Decision | Chosen Approach | Alternative Considered | Rationale |
|----------|-----------------|----------------------|-----------|
| **Protocol** | MCP (Model Context Protocol) | REST + GraphQL | MCP enables runtime tool discovery — agents self-assemble workflows without code changes |
| **LMS** | Headless Moodle | Custom LMS | Moodle is proven at scale in Indian education; headless mode gives us API control |
| **AI Model** | Gemini 3 Pro | GPT-4, Claude, Llama | Superior multimodal reasoning (handwriting + diagrams), cost-effective at scale |
| **Graph DB** | Neo4j | PostgreSQL + recursive CTEs | Native graph traversal for prerequisite chains; performs 10x better for path queries |
| **Edge Computing** | Astra Hub (custom) | Chromebooks + Cloud-only | India's connectivity reality demands offline-first; custom hub controls the full UX |
| **Content Format** | JSON-first structured | Markdown / HTML | JSON enables programmatic manipulation by AI agents; rendered to any frontend |
| **Analytics** | ClickHouse | PostgreSQL / TimescaleDB | Column-oriented storage is ideal for aggregation-heavy analytics queries |

---

## 12. Glossary

| Term | Definition |
|------|------------|
| **MCP** | Model Context Protocol — an open standard for AI agents to discover and invoke tools |
| **Mastery Tree** | A directed acyclic graph (DAG) of concepts where edges represent prerequisite dependencies |
| **Mastery Node** | A student's proficiency record for a single concept, including score, misconceptions, and history |
| **Transfer Task** | An assessment that requires applying a concept to an unfamiliar, real-world context |
| **Astra Hub** | A low-cost edge server deployed in schools for offline-first operation and local printing |
| **Bloom's Level** | Bloom's Taxonomy classification (Remember → Understand → Apply → Analyze → Evaluate → Create) |
| **Comprehension Heatmap** | Real-time visualization of class-wide understanding levels per concept |
| **Shadow Mode** | Background observer agents that track learning metrics without affecting the student experience |
| **AI Factory** | The multi-agent pipeline that converts raw textbooks into interactive, mastery-aligned courses |
| **Synthetic Student** | An AI-simulated learner persona used for automated course quality testing |
| **DPDPA** | Digital Personal Data Protection Act, 2023 — India's data privacy legislation |

---

<div align="center">

**Built with ❤️ for every student in India**

*Because understanding should never be a privilege — it should be a pathway.*

</div>
