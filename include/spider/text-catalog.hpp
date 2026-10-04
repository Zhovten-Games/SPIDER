// SPDX-License-Identifier: MIT
#pragma once
#include <optional>
#include <string>
#include <utility>
#include <vector>

namespace spider {
struct TextEntry { std::string key; std::string locale; std::string text; };
struct ResolvedText {
    std::string key;
    std::string requested_locale;
    std::string served_locale;
    std::string text;
    bool is_fallback{};
};
class TextCatalog {
public:
    TextCatalog(std::vector<TextEntry> entries, std::string fallback_locale)
        : entries_(std::move(entries)), fallback_locale_(std::move(fallback_locale)) {}
    [[nodiscard]] std::optional<ResolvedText> resolve(const std::string& key,
                                                     const std::string& locale) const {
        for (const auto& entry : entries_) {
            if (entry.key == key && entry.locale == locale)
                return ResolvedText{key, locale, locale, entry.text, false};
        }
        for (const auto& entry : entries_) {
            if (entry.key == key && entry.locale == fallback_locale_)
                return ResolvedText{key, locale, fallback_locale_, entry.text, true};
        }
        return std::nullopt;
    }
    [[nodiscard]] const std::string& fallback_locale() const { return fallback_locale_; }
private:
    std::vector<TextEntry> entries_;
    std::string fallback_locale_;
};
} // namespace spider
