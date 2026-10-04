// SPDX-License-Identifier: MIT
#include <spider/check-result.hpp>
#include <spider/command-context.hpp>
#include <spider/text-catalog.hpp>
#include <iostream>

int main() {
    spider::CheckLedger checks;
    const auto record_bool = [&](const std::string& id, bool result) {
        checks.record(id, "true", result ? "true" : "false");
    };
    record_bool("context.current", spider::check_command_context({"c1", 2}, 2) == spider::ContextError::none);
    record_bool("context.stale", spider::check_command_context({"c1", 1}, 2) == spider::ContextError::stale_revision);
    record_bool("context.empty", spider::check_command_context({"", 2}, 2) == spider::ContextError::empty_command_id);
    const spider::TextCatalog catalog({{"hello", "ru", "Привет"}, {"hello", "en", "Hello"}}, "ru");
    const auto en = catalog.resolve("hello", "en");
    const auto fallback = catalog.resolve("hello", "uk");
    record_bool("locale.exact", en && en->text == "Hello" && !en->is_fallback);
    record_bool("locale.fallback", fallback && fallback->served_locale == "ru" && fallback->is_fallback);
    record_bool("locale.missing", !catalog.resolve("unknown", "en"));
    for (const auto& result : checks.results())
        std::cout << result.id << " expected=" << result.expected << " actual=" << result.actual << '\n';
    return checks.is_passed() ? 0 : 1;
}
