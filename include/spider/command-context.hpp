// SPDX-License-Identifier: MIT
#pragma once
#include <cstdint>
#include <string>

namespace spider {
struct CommandContext {
    std::string command_id;
    std::uint64_t expected_revision{};
};
enum class ContextError { none, empty_command_id, stale_revision };
inline ContextError check_command_context(const CommandContext& context,
                                           std::uint64_t revision) {
    if (context.command_id.empty()) return ContextError::empty_command_id;
    if (context.expected_revision != revision) return ContextError::stale_revision;
    return ContextError::none;
}
} // namespace spider
