"""Gate the daily-problem picker behind a LaunchDarkly flag.

Exists to give Hyrax Change Review one flag reference to look up, so a run
shows whether the LaunchDarkly integration answered.
"""


def use_new_picker(ld_client, context) -> bool:
    return ld_client.variation("hyrax-ld-smoke-test", context, False)
