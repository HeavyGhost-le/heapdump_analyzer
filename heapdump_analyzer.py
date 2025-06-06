<h1>Heap Dump Forensic Analysis Report</h1>
<p>Generated: 2025-04-28 12:34:56</p>
<div class="card">
  <div class="card-header">Analysis Summary</div>
  <p>File: heap.dump</p>
  <p>Total strings analyzed: 1,000</p>
  <p>Unique classes identified: 50</p>
</div>
<div class="card">
  <div class="card-header">Risk Assessment</div>
  <p>Overall Risk Score: 75.0/100</p>
  <div class="risk-meter"><div class="risk-indicator"></div></div>
  <table>
    <tr><th>Type</th><th>Severity</th><th>Description</th></tr>
    <tr class="critical"><td>exposed_private_key</td><td>critical</td><td>Private cryptographic key found in memory</td></tr>
    ...
  </table>
</div>
<div class="card">
  <div class="card-header">HTTP Sessions (Top 5)</div>
  <h3>Session 1 (Confidence: 85%)</h3>
  <p>Requests: 3 | Methods: GET, POST</p>
  ...
</div>
...