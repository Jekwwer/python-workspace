module.exports = {
  branches: [
    'main',
    { name: 'next', prerelease: true },
    { name: 'beta', prerelease: true },
    { name: 'alpha', prerelease: true },
  ],
  plugins: [
    [
      '@semantic-release/commit-analyzer',
      {
        preset: 'conventionalcommits',
        // Explicit list (including default-equivalent rules) self-documents
        // the full project commit-type policy.
        releaseRules: [
          { breaking: true, release: 'major' },
          { type: 'init', release: false },
          { type: 'feat', release: 'minor' },
          { type: 'security', release: 'patch' },
          { type: 'fix', release: 'patch' },
          { type: 'perf', release: 'patch' },
          // revert: handled by semantic-release auto-cancel (pairs with reverted commit, excluded from release)
          { type: 'deps', release: 'patch' },
          { type: 'build', release: 'patch' },
          { type: 'docs', release: false },
          { type: 'refactor', release: false },
          { type: 'style', release: false },
          { type: 'test', release: false },
          { type: 'chore', release: false },
          { type: 'ci', release: false },
        ],
      },
    ],
    [
      '@semantic-release/release-notes-generator',
      {
        preset: 'conventionalcommits',
        presetConfig: {
          types: [
            { type: 'init', section: '🎉 Initial Commit', hidden: true },
            { type: 'feat', section: '🚀 New Features' },
            { type: 'security', section: '🔒 Security Updates' },
            { type: 'fix', section: '🐞 Bug Fixes' },
            { type: 'perf', section: '⚡ Performance Improvements' },
            { type: 'revert', section: '⏪ Reverts' },
            { type: 'deps', section: '📦 Dependency Updates' },
            { type: 'build', section: '🏗️ Build System' },
            { type: 'docs', section: '📖 Documentation' },
            { type: 'refactor', section: '🛠️ Refactoring', hidden: true },
            { type: 'style', section: '🎨 Code Style Improvements', hidden: true },
            { type: 'test', section: '✅ Testing', hidden: true },
            { type: 'chore', section: '🔧 Chores' },
            { type: 'ci', section: '🔄 Continuous Integration' },
          ],
        },
        writerOpts: {
          headerPartial: '## {{version}} - {{date}}',
          // Upstream template hardcodes `⚠` (U+26A0) without VS-16, which renders
          // as text-style glyph alongside emoji-style section icons. Override to
          // append U+FE0F so it renders as colored emoji.
          mainTemplate:
            '{{> header}}\n' +
            '{{#if noteGroups}}\n' +
            '{{#each noteGroups}}\n' +
            '\n' +
            '### ⚠️ {{title}}\n' +
            '\n' +
            '{{#each notes}}\n' +
            '* {{#if commit.scope}}**{{commit.scope}}:** {{/if}}{{text}}\n' +
            '{{/each}}\n' +
            '{{/each}}\n' +
            '{{/if}}\n' +
            '{{#each commitGroups}}\n' +
            '\n' +
            '{{#if title}}\n' +
            '### {{title}}\n' +
            '\n' +
            '{{/if}}\n' +
            '{{#each commits}}\n' +
            '{{> commit root=@root}}\n' +
            '{{/each}}\n' +
            '{{/each}}\n',
          groupBy: 'type',
          commitGroupsSort: (a, b) => {
            const order = [
              '🎉 Initial Commit',
              '🚀 New Features',
              '🔒 Security Updates',
              '🐞 Bug Fixes',
              '⚡ Performance Improvements',
              '⏪ Reverts',
              '📦 Dependency Updates',
              '🏗️ Build System',
              '📖 Documentation',
              '🛠️ Refactoring',
              '🎨 Code Style Improvements',
              '✅ Testing',
              '🔧 Chores',
              '🔄 Continuous Integration',
            ];
            return order.indexOf(a.title) - order.indexOf(b.title);
          },
          commitsSort: ['scope', 'subject'],
        },
      },
    ],
    [
      '@semantic-release/changelog',
      {
        changelogFile: 'CHANGELOG.md',
        changelogTitle: '# Changelog',
      },
    ],
    [
      '@semantic-release/npm',
      {
        npmPublish: false,
      },
    ],
    [
      '@semantic-release/github',
      {
        assets: [
          { path: 'dist/*.whl', label: 'Python wheel' },
          { path: 'dist/*.tar.gz', label: 'Source distribution (sdist)' },
        ],
      },
    ],
    [
      '@semantic-release/exec',
      {
        prepareCmd: `
        sed -i -E "s/v[0-9]+\\.[0-9]+\\.[0-9]+/v\${nextRelease.version}/g" SECURITY.md &&
        sed -i "s/^version = \\".*\\"/version = \\"\${nextRelease.version}\\"/" pyproject.toml &&
        sed -i -E "s/Copyright \\(c\\) ([0-9]{4})(–[0-9]{4})?/Copyright (c) \\1–$(date +%Y)/" LICENSE &&
        poetry build
      `,
      },
    ],
    [
      '@semantic-release/git',
      {
        assets: [
          'package.json',
          'package-lock.json',
          'pyproject.toml',
          'CHANGELOG.md',
          'SECURITY.md',
          'LICENSE',
        ],
        message:
          'chore(release): ${nextRelease.version} [skip ci]\n\n${nextRelease.notes}',
      },
    ],
  ],
};
