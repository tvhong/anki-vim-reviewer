# Anki GUI Hooks Reference

## Overview

- `overview_did_refresh`
- `overview_will_render_content`
- `overview_will_render_bottom`

## Reviewer

- `reviewer_did_show_question`
- `reviewer_will_compare_answer`
- `reviewer_will_render_compared_answer`
- `reviewer_did_show_answer`
- `reviewer_will_init_answer_buttons`
- `reviewer_will_answer_card`
- `reviewer_did_answer_card`
- `reviewer_will_show_context_menu`
- `reviewer_will_end`
- `reviewer_will_play_question_sounds`
- `reviewer_will_play_answer_sounds`
- `reviewer_will_replay_recording`
- `reviewer_will_suspend_note`
- `reviewer_will_suspend_card`
- `reviewer_will_bury_note`
- `reviewer_will_bury_card`
- `reviewer_did_init`
- `card_will_show`
- `card_review_webview_did_init`

## Debug

- `debug_console_will_show`
- `debug_console_did_evaluate_python`

## Card Layout

- `card_layout_will_show`

## Deck Browser

- `deck_browser_did_render`
- `deck_browser_will_render_content`

## Deck Options (Legacy Screen)

- `deck_conf_did_setup_ui_form`
- `deck_conf_will_show`
- `deck_conf_did_load_config`
- `deck_conf_will_save_config`
- `deck_conf_did_add_config`
- `deck_conf_will_remove_config`
- `deck_conf_will_rename_config`

## Deck Options (New Screen)

- `deck_options_did_load`

## Filtered Deck Options

- `filtered_deck_dialog_did_load_deck`
- `filtered_deck_dialog_will_add_or_update_deck`
- `filtered_deck_dialog_did_add_or_update_deck`

## Browser

- `default_search`
- `browser_will_show`
- `browser_menus_did_init`
- `browser_will_show_context_menu`
- `browser_sidebar_will_show_context_menu`
- `browser_header_will_show_context_menu`
- `browser_did_change_row`
- `browser_will_build_tree`
- `browser_will_search`
- `browser_did_search`
- `browser_did_fetch_row`
- `browser_did_fetch_columns`

## Previewer

- `previewer_did_init`
- `previewer_will_redraw_after_show_both_sides_toggled`

## Main Window States

- `state_will_change`
- `state_did_change`
- `state_shortcuts_will_change`

## UI State/Refreshing

- `state_did_undo`
- `state_did_reset`
- `operation_did_execute`
- `focus_did_change`
- `backend_will_block`
- `backend_did_block`
- `theme_did_change`
- `body_classes_need_update`

## Webview

- `webview_did_receive_js_message`
- `webview_will_set_content`
- `webview_will_show_context_menu`
- `webview_did_inject_style_into_page`

## Main

- `main_window_did_init`
- `main_window_should_require_reset`
- `backup_did_complete`
- `profile_did_open`
- `profile_will_close`
- `collection_will_temporarily_close`
- `collection_did_temporarily_close`
- `collection_did_load`
- `undo_state_did_change`
- `style_did_init`
- `top_toolbar_did_init_links`
- `top_toolbar_will_set_left_tray_content`
- `top_toolbar_will_set_right_tray_content`
- `top_toolbar_did_redraw`
- `media_sync_did_progress`
- `media_sync_did_start_or_stop`
- `empty_cards_will_show`
- `sync_will_start`
- `sync_did_finish`
- `media_check_will_start`
- `media_check_did_finish`
- `day_did_change`

## Importing/Exporting Data

- `exporter_will_export`
- `exporter_did_export`
- `legacy_exporter_will_export`
- `legacy_exporter_did_export`
- `exporters_list_did_initialize`

## Dialog Manager

- `dialog_manager_did_open_dialog`

## Adding Cards

- `add_cards_will_show_history_menu`
- `add_cards_did_init`
- `add_cards_did_add_note`
- `add_cards_will_add_note`
- `add_cards_might_add_note`
- `addcards_will_add_history_entry`
- `add_cards_did_change_note_type`
- `addcards_did_change_note_type`
- `add_cards_did_change_deck`

## Editing

- `editor_did_init_left_buttons`
- `editor_did_init_buttons`
- `editor_did_init_shortcuts`
- `editor_will_show_context_menu`
- `editor_did_fire_typing_timer`
- `editor_did_focus_field`
- `editor_did_unfocus_field`
- `editor_did_load_note`
- `editor_did_update_tags`
- `editor_will_munge_html`
- `editor_will_use_font_for_field`
- `editor_web_view_did_init`
- `editor_did_init`
- `editor_will_load_note`
- `editor_did_paste`
- `editor_will_process_mime`
- `editor_state_did_change`
- `editor_mask_editor_did_load_image`

## Tag

- `tag_editor_did_process_key`

## Sound/Video

- `av_player_will_play`
- `av_player_did_begin_playing`
- `av_player_did_end_playing`
- `av_player_will_play_tags`
- `audio_will_replay`
- `audio_did_pause_or_unpause`
- `audio_did_seek_relative`

## Addon

- `addon_config_editor_will_display_json`
- `addon_config_editor_will_save_json`
- `addon_config_editor_will_update_json`
- `addons_dialog_will_show`
- `addons_dialog_did_change_selected_addon`
- `addons_dialog_will_delete_addons`
- `addon_manager_will_install_addon`
- `addon_manager_did_install_addon`

## Model

- `models_advanced_will_show`
- `models_did_init_buttons`

## Fields

- `fields_did_add_field`
- `fields_did_rename_field`
- `fields_did_delete_field`

## Stats

- `stats_dialog_will_show`
- `stats_dialog_old_will_show`

## Other

- `current_note_type_did_change`
- `sidebar_should_refresh_decks`
- `sidebar_should_refresh_notetypes`
- `deck_browser_will_show_options_menu`
- `flag_label_did_change`

---

**Total: 136 hooks**

These hooks provide extensive customization points throughout Anki's GUI application, allowing add-ons to modify behavior across reviewing, browsing, editing, deck management, sync operations, and many other aspects of the application.
