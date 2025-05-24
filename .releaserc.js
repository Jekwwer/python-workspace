// .releaserc.js: Configures the semantic-release process.
module.exports = {
  branches: ['main'],
  plugins: [
    [
      '@semantic-release/commit-analyzer',
      {
        preset: 'conventionalcommits',
        releaseRules: [
          { type: 'init', release: false },
          { type: 'feat', release: 'minor' },
          { type: 'fix', release: 'patch' },
          { type: 'security', release: 'patch' },
          { type: 'deps', release: 'patch' },
          { type: 'docs', release: false },
          { type: 'docs', scope: 'api', release: 'patch' },
          { type: 'style', release: false },
          { type: 'refactor', release: false },
          { type: 'chore', release: false },
          { type: 'chore', scope: 'sync', release: 'patch' },
          { type: 'ci', release: false },
          { type: 'test', scope: 'critical', release: 'patch' },
          { type: 'test', release: false },
        ],
      },
    ],
    [
      '@semantic-release/release-notes-generator',
      {
        preset: 'conventionalcommits',
        presetConfig: {
          header: '# Release Notes',
          types: [
            { type: 'init', section: '🎉 Initial Commit', hidden: true },
            { type: 'feat', section: '🚀 New Features' },
            { type: 'fix', section: '🐞 Bug Fixes' },
            { type: 'security', section: '🔒 Security Updates' },
            { type: 'deps', section: '📦 Dependency Updates' },
            { type: 'docs', section: '📖 Documentation' },
            { type: 'test', section: '✅ Testing' },
            { type: 'perf', section: '⚡ Performance Improvements' },
            { type: 'chore', section: '📦 Chores' },
            { type: 'style', section: '🎨 Code Style Improvements' },
            { type: 'refactor', section: '🛠️ Refactoring' },
            { type: 'ci', section: '🔄 Continuous Integration' },
          ],
        },
        writerOpts: {
          headerPartial: '## {{version}} - {{date}}',
          groupBy: 'type',
          commitGroupsSort: (a, b) => {
            const order = [
              '🎉 Initial Commit',
              '🚀 New Features',
              '🐞 Bug Fixes',
              '🔒 Security Updates',
              '📦 Dependency Updates',
              '📖 Documentation',
              '✅ Testing',
              '⚡ Performance Improvements',
              '📦 Chores',
              '🎨 Code Style Improvements',
              '🛠️ Refactoring',
              '🔄 Continuous Integration',
            ];
            return order.indexOf(a.title) - order.indexOf(b.title);
          },
          commitsSort: ['scope', 'subject'],
        },
        linkCompare: true,
        linkReferences: true,
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
        successComment:
          ":tada: This ${issue.pull_request ? 'pull request' : 'issue'} has been included in version ${nextRelease.version} :tada:\n\nThe release is available on [GitHub release](${releases[0].url}).",
        failComment:
          "The release from branch ${branch.name} failed due to the following issues:\n\n${errors.map(e => `- ${e.message}`).join('\\n')}",
        failTitle: 'The automated release failed 🚨',
        releasedLabels: [
          "released<%= nextRelease.channel ? ` on @${nextRelease.channel}` : '' %>",
        ],
      },
    ],
    [
      '@semantic-release/exec',
      {
        prepareCmd: `
        sed -i -E "s/v[0-9]+\\.[0-9]+\\.[0-9]+/v\${nextRelease.version}/g" SECURITY.md &&
        sed -i "s/^version = \\".*\\"/version = \\"\${nextRelease.version}\\"/" pyproject.toml &&
        sed -i "s/^__version__ = \\".*\\"/__version__ = \\"\${nextRelease.version}\\"/" src/python_workspace/__init__.py &&
        sed -i "s/^release = \\".*\\"/release = \\"\${nextRelease.version}\\"/" docs/source/conf.py
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
          'src/python_workspace/__init__.py',
          'docs/source/conf.py',
          'CHANGELOG.md',
          'SECURITY.md',
        ],
        message:
          'chore(release): ${nextRelease.version} [skip ci]\n\n${nextRelease.notes}',
      },
    ],
  ],
};
