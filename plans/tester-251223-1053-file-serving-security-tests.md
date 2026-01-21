# Action Plan: File Serving Security Integration Tests

**Created:** 2025-12-23 10:53 UTC
**Priority:** CRITICAL
**Owner:** QA / Security
**Base Directory:** `.claude/skills/marketing-dashboard/server`

---

## Task List

### Phase 1: Create Security Test Suite

#### Task 1.1: Setup Integration Test File
- **File:** `__tests__/security-file-serving.test.js`
- **Tests Required:** 12-15 security + functional tests
- **Framework:** vitest + hono/testing (built into Hono)

#### Task 1.2: Path Traversal Bypass Vector Tests
Test all 6 security layers:

**Bypass Attempts (All should return 403):**

1. Windows backslashes: `..\..\etc\passwd`
2. Leading slashes: `/../etc/passwd`
3. URL encoded basic: `%2e%2e%2fetc/passwd`
4. Double URL encoded: `%252e%252e%252f`
5. Mixed separators: `..\../etc/passwd`
6. Backslash + dots: `\\..\\..\\etc\\passwd`
7. Null byte (if applicable): `..%00/etc/passwd`
8. Backslash normalization bypass: `..\\\\..\\\\etc`
9. Multiple dots: `....//etc/passwd` (variant)
10. Unicode variations: `％2e％2e／etc/passwd` (if UTF-8)

#### Task 1.3: Valid File Access Tests
- Create test asset files in `__tests__/fixtures/`
- Test successful file serving (200 response)
- Verify binary content returned
- Check appropriate Content-Type headers

#### Task 1.4: Error Scenario Tests
- Non-existent file (404)
- Directory without slash (403 or 404)
- Empty path (403)
- Very long paths (403 or 414)

### Phase 2: Create Test Fixtures

#### Task 2.1: Test Asset Files
- Create `__tests__/fixtures/assets/` directory
- Add sample files: image.png, document.txt, data.json
- Create subdirectories: `__tests__/fixtures/assets/subfolder/`

#### Task 2.2: Mock Assets Directory
- Configure vitest to mock assets directory path
- Ensure tests don't require actual /assets folder

### Phase 3: Validation & Reporting

#### Task 3.1: Run Security Tests
```bash
npm test -- __tests__/security-file-serving.test.js
```

#### Task 3.2: Verify All Tests Pass
- 12+ security tests passing
- 100% bypass attempts returning 403
- Valid file access returning 200

#### Task 3.3: Generate Coverage
```bash
npm test -- --coverage __tests__/security-file-serving.test.js
```

#### Task 3.4: Update Main Test Report
- Add security test results to main report
- Confirm all 111 + security tests passing

---

## Test Code Template

### Basic Structure

```javascript
import { describe, it, expect, beforeEach, afterEach } from 'vitest';
import { Hono } from 'hono';
import assetsRouter from '../routes/assets.js';
import { join } from 'path';
import { mkdirSync, writeFileSync } from 'fs';

describe('Asset File Serving Security', () => {
  let app;
  const fixturesDir = join(__dirname, 'fixtures/assets');

  beforeEach(() => {
    app = new Hono();
    app.route('/api/assets', assetsRouter);

    // Setup fixture files
    mkdirSync(fixturesDir, { recursive: true });
    writeFileSync(join(fixturesDir, 'test.txt'), 'test content');
  });

  describe('Path Traversal Prevention', () => {
    it('should block Windows backslashes', () => {
      // Test: GET /api/assets/file/..\..\etc\passwd
      // Expected: 403 Access denied
    });

    it('should block URL encoded attempts', () => {
      // Test: GET /api/assets/file/%2e%2e%2fetc/passwd
      // Expected: 403 Access denied
    });

    // ... more tests
  });

  describe('Valid File Access', () => {
    it('should serve valid files successfully', () => {
      // Test: GET /api/assets/file/test.txt
      // Expected: 200 + file content
    });
  });
});
```

---

## Success Criteria

- [ ] All 12+ security tests written and passing
- [ ] All 6 bypass vectors tested and blocked (403)
- [ ] Valid file access working (200)
- [ ] Coverage report shows routes/assets.js /file/* endpoint tested
- [ ] No performance regression (< 100ms per request)
- [ ] All 111 existing tests still passing
- [ ] Security test report merged into main report

---

## Estimated Effort

| Task | Effort | Timeline |
|------|--------|----------|
| Write security tests | 2-3 hours | 1 day |
| Create test fixtures | 30 min | 1 day |
| Run & debug | 1-2 hours | 1 day |
| Update reports | 30 min | 1 day |
| **Total** | **4-6 hours** | **1 day** |

---

## Blockers / Dependencies

- Need to ensure test fixtures directory structure matches actual assets location
- May need to mock file system if tests should be fast & isolated
- vitest should support hono app testing directly (verify)

---

## Notes

- Phase 2 security implementation is GOOD but untested
- Without these tests, security claims are unvalidated
- Integration tests are MORE important than unit tests for file serving
- Consider using supertest for more realistic HTTP testing if direct Hono testing insufficient
