// SPDX-License-Identifier: MIT
#pragma once
#include <algorithm>
#include <string>
#include <utility>
#include <vector>

namespace spider {
struct CheckResult {
    std::string id;
    std::string expected;
    std::string actual;
    bool is_passed{};
};
class CheckLedger {
public:
    void record(std::string id, std::string expected, std::string actual) {
        const bool is_passed = expected == actual;
        results_.push_back({std::move(id), std::move(expected), std::move(actual), is_passed});
    }
    [[nodiscard]] const std::vector<CheckResult>& results() const { return results_; }
    [[nodiscard]] bool is_passed() const {
        return std::all_of(results_.begin(), results_.end(),
                           [](const auto& result) { return result.is_passed; });
    }
private:
    std::vector<CheckResult> results_;
};
} // namespace spider
