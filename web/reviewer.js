// Anki Vim Reviewer - JavaScript
// Movement keys are handled by Python VimKeyEventFilter
//
// Copyright: (c) 2025 Vy Hong <shiweistg@gmail.com>
// License: GNU AGPLv3 <https://www.gnu.org/licenses/agpl.html>

let currentSearchState = {
    mode: "inactive",
    query: "",
    currentMatch: 0,
    totalMatches: 0,
    isInputActive: false,
};

let searchUI = null;

function createSearchUI() {
    const searchContainer = document.createElement("div");
    searchContainer.id = "vim-search-container";
    searchContainer.style.cssText = `
        position: fixed;
        bottom: 0;
        left: 0;
        right: 0;
        background: #333;
        color: white;
        padding: 8px 12px;
        font-family: monospace;
        font-size: 14px;
        border-top: 1px solid #666;
        z-index: 10000;
        display: none;
    `;

    const searchPrefix = document.createElement("span");
    searchPrefix.id = "vim-search-prefix";
    searchPrefix.textContent = "/";

    const searchQuery = document.createElement("span");
    searchQuery.id = "vim-search-query";
    searchQuery.style.cssText = `
        margin-left: 4px;
        background: transparent;
        border: none;
        outline: none;
        color: white;
        font-family: inherit;
        font-size: inherit;
    `;

    const searchStatus = document.createElement("span");
    searchStatus.id = "vim-search-status";
    searchStatus.style.cssText = `
        float: right;
        color: #aaa;
        font-size: 12px;
    `;

    searchContainer.appendChild(searchPrefix);
    searchContainer.appendChild(searchQuery);
    searchContainer.appendChild(searchStatus);
    document.body.appendChild(searchContainer);

    searchUI = {
        container: searchContainer,
        prefix: searchPrefix,
        query: searchQuery,
        status: searchStatus,
    };

    return searchUI;
}

function refresh(state) {
    if (!searchUI) {
        createSearchUI();
    }

    currentSearchState = { ...currentSearchState, ...state };

    const { container, prefix, query, status } = searchUI;

    if (currentSearchState.mode === "inactive") {
        container.style.display = "none";
        return;
    }

    // Show search bar
    container.style.display = "block";

    // Update prefix based on search mode
    prefix.textContent = currentSearchState.mode === "forward" ? "/" : "?";

    // Update query display
    query.textContent = currentSearchState.query;

    // Add cursor if input is active
    if (currentSearchState.isInputActive) {
        query.textContent += "|";
    }

    // Update status
    if (currentSearchState.totalMatches > 0) {
        status.textContent = `${currentSearchState.currentMatch + 1}/${currentSearchState.totalMatches}`;
    } else if (currentSearchState.query && !currentSearchState.isInputActive) {
        status.textContent = "No matches";
    } else {
        status.textContent = "";
    }
}

function performSearch(query, direction) {
    if (!query) return;

    const searchResult = window.find(
        query,
        false,
        direction === "backward",
        true,
    );

    // Basic match counting (not perfect but functional)
    const textContent =
        document.body.textContent || document.body.innerText || "";
    const matches =
        textContent.toLowerCase().split(query.toLowerCase()).length - 1;

    currentSearchState.totalMatches = matches;
    currentSearchState.currentMatch = searchResult ? 1 : 0;

    // Update the display
    refresh(currentSearchState);
}

function searchNext() {
    if (!currentSearchState.query) return;

    const found = window.find(currentSearchState.query, false, false, true);
    if (
        found &&
        currentSearchState.currentMatch < currentSearchState.totalMatches
    ) {
        currentSearchState.currentMatch++;
        refresh(currentSearchState);
    }
}

function searchPrevious() {
    if (!currentSearchState.query) return;

    const found = window.find(currentSearchState.query, false, true, true);
    if (found && currentSearchState.currentMatch > 1) {
        currentSearchState.currentMatch--;
        refresh(currentSearchState);
    }
}

document.addEventListener("DOMContentLoaded", function () {
    console.log("Anki Vim Reviewer JavaScript loaded");
    createSearchUI();
});
