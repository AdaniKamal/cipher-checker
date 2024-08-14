# Cipher checker

## Problem
With the extensive list of cipher suites available, it can be challenging for security professionals <b> to quickly determine the security status of a given cipher suite </b>. Manually checking each cipher against security databases is time-consuming especially when dealing with multiple ciphers. 
There is a need for a streamlined, automated solution that can efficiently evaluate the security status of one or multiple cipher suites and provide clear, color-coded feedback.

## Objective
To develop a Python-based tool, Cipher Checker, that automates the process of assessing the security status of cipher suites. The tool should allow users to either check a single cipher or scan a file containing multiple ciphers. The results should be presented in a user-friendly, color-coded format that highlights the security status of each cipher.

## Key Features
<b>1. Single Cipher Check:</b> Users can input a single cipher suite name and receive an immediate security assessment. <br>
<b>2. Bulk Cipher Check:</b> Users can provide a file containing multiple cipher suite names for batch processing. <br>
<b>3. Color-Coded Output:</b> The tool will display the security status of each cipher in a color-coded manner:
- Weak: Orange
- Insecure: Red
- Recommended: Blue
- Secure: Green
4. <b> Command-Line Interface:</b> The tool will operate via the command line, providing flexibility for integration into larger security auditing processes.

## Expected Outcome:
The CipherCheck tool will enable security professionals to efficiently evaluate the security of cipher suites.

Our main reference is [CipherSuite Info](https://ciphersuite.info)
