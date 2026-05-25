#!/bin/bash

# Script to run the Orders page tests

echo "=========================================="
echo "Running Orders Page Tests"
echo "=========================================="

# Run test 1: Orders page loads after login
echo ""
echo "Test 1: Verify Orders Page Loads After Login"
pytest Test/test_orders.py::test_verify_orders_page_loads_after_login -v -s --headed --slowmo=500

# Run test 2: Order search functionality
echo ""
echo "Test 2: Verify Order Search Functionality"
pytest Test/test_orders.py::test_verify_order_search_functionality -v -s --headed --slowmo=500

echo ""
echo "=========================================="
echo "All tests completed!"
echo "=========================================="
