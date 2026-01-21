# User Testing Scripts & Templates

> **Used by**: QA Agent
> **When**: Creating customized testing materials

---

## The 10-Second Test

### Purpose
Reveals what visitors remember and understand from the first impression. Validates headline, value proposition, and design clarity.

### Who Should Do It
Everyone. This is the minimum viable test for any landing page.

### Process

#### Step 1: Define Success Criteria
Write down 3-5 things the page MUST communicate:
```
1. What the product/service is
2. Who it's for
3. The primary benefit
4. What action to take
5. Why trust this company
```

#### Step 2: Find Participants
- 5-8 people from target audience
- Friends/family if target audience unavailable
- Avoid people who've seen the page before

#### Step 3: Conduct the Test

**Script**:
```
"I'm going to show you a website for just 10 seconds.
Look at it normally—don't try to memorize anything.
After 10 seconds, I'll hide it and ask you a few questions."
```

**Process**:
1. Share screen showing the landing page
2. Say "Go" and start 10-second timer
3. At exactly 10 seconds, close/hide the page
4. Ask the questions below

#### Step 4: Questions

1. "What do you remember from that page?"
   (Let them answer freely first)

2. "What was this website or product about?"

3. "Who do you think this is designed for?"

4. "Would you be interested in learning more? Why or why not?"

5. "Was anything confusing or unclear?"

### Recording Results

| Participant | Remembered | Understood Product | Understood Audience | Interest (1-5) |
|-------------|------------|-------------------|---------------------|----------------|
| P1 | | | | |
| P2 | | | | |
| P3 | | | | |

### Success Criteria
- ✅ PASS: 4/5 correctly identify what the product does
- ✅ PASS: 4/5 correctly identify target audience
- ✅ PASS: 3/5 express interest in learning more
- ⚠️ FLAG: Headline not remembered by majority
- ⚠️ FLAG: Main value prop misunderstood

---

## Full User Testing Script

### Setup (2 minutes)

**Read to participant**:
```
"Hi, I'm [name], and I'm working on [product]. Thank you for helping today.

Before we start:

1. This is a test of the website, not of you. There are no wrong answers.

2. If anything is confusing, that's valuable feedback—it means we need to fix it.

3. Please be completely honest, even if it feels harsh. You won't offend anyone.

4. I'd like you to think out loud as much as possible. Tell me what you're
   looking at, what you're thinking, what confuses you.

5. Feel free to ask questions, but I'll try not to answer until the end.

Is it okay if I record this session? The recording is only for our team.

Do you have any questions before we begin?"
```

### Scenario (1 minute)

**Customize based on target audience**:
```
"Imagine you're a [target audience] who is struggling with [pain point].
A friend recommended this product to help.

Please type this URL: [URL]

Go ahead and open it."
```

### 10-Second Test (30 seconds)
```
"Before you start exploring, look at this page for about 10 seconds
without clicking anything."

[Wait 10 seconds]

"Please look away from the screen.
What do you remember from what you just saw?
What do you think this product or service does?"
```

### Free Exploration (8-10 minutes)

```
"Great, you can look back now and start exploring.
Your task is to decide whether you would [primary conversion action].
Please think out loud as you go."
```

**Prompts if they go quiet** (10+ seconds):
- "What are you looking at right now?"
- "What are you thinking?"
- "What's going through your mind?"

**If they seem confused**:
- "You seem uncertain—what's happening?"
- "What were you expecting to see there?"

**If they react visibly**:
- "I noticed a reaction. What was that about?"

### Observation Checklist

- [ ] Where did they click first?
- [ ] What sections did they scroll past quickly?
- [ ] What sections did they spend time reading?
- [ ] Did they use the navigation?
- [ ] Did they notice social proof?
- [ ] Did they understand pricing (if shown)?
- [ ] Any visible confusion or frustration?
- [ ] Did they interact with the CTA?

### Conclusion Questions (5 minutes)

```
"Thanks for exploring. I have a few final questions."
```

1. "In your own words, what does this product do?"

2. "Who do you think this product is designed for?"

3. "If you were considering [conversion], what would be your biggest
    hesitation or concern?"

4. "Was there anything on the page that was confusing or unclear?"

5. "Was there anything you wanted to know that wasn't on the page?"

6. "On a scale of 1-10, how interested are you in this product?"

7. "What would make you more likely to [conversion]?"

**Add custom questions for each objection**:
8. "[Question about objection 1]"
9. "[Question about objection 2]"
10. "[Question about objection 3]"

### Wrap Up

```
"That's everything. Thank you—this was incredibly helpful.

Do you have any questions for me now?

[If offering compensation]: I'll send your [gift card/payment] within 24 hours.

Thanks again!"
```

---

## Analysis Template

### Per Participant

| Category | Notes |
|----------|-------|
| Participant ID | |
| Date/Time | |
| Duration | |
| 10-sec recall | |
| Product understanding | Correct / Partial / Incorrect |
| Audience understanding | Correct / Partial / Incorrect |
| Interest level (1-10) | |
| Main hesitation | |
| Confusing parts | |
| Missing information | |
| Key quotes | |
| Recommendations | |

### Aggregate Analysis

| Metric | Target | Actual |
|--------|--------|--------|
| Correct product understanding | 4/5 | /5 |
| Correct audience understanding | 4/5 | /5 |
| Average interest score | ≥7 | |
| Would take action | ≥3/5 | /5 |

### Objection Coverage

| Objection | Raised Unprompted | Target |
|-----------|------------------|--------|
| [Objection 1] | /5 | <2/5 |
| [Objection 2] | /5 | <2/5 |
| [Objection 3] | /5 | <2/5 |

---

## Finding Participants

### For Specific Audiences
- LinkedIn (filter by job title)
- Industry forums/communities
- Existing customer base
- Friends of friends referrals

### General Testing
- UserTesting.com (paid, with screening)
- Friends and family (free, less accurate)

### Incentives
- $20-50 gift cards for 20-minute sessions
- Amazon, PayPal, or industry-specific rewards

---

## Red Flags (Require Revision)

- [ ] Majority misunderstand the product
- [ ] Main CTA not noticed
- [ ] Consistent confusion on same element
- [ ] Average interest <5/10
- [ ] Same objection raised by 3+ participants
