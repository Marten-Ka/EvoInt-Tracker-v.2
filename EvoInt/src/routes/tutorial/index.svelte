<script lang="ts">
	import Header from '../../components/Header.svelte';
	import AnimationContainer from '../../components/AnimationContainer.svelte';
	import TutorialRedirectButton from './_TutorialRedirectButton.svelte';

	const redirects = [
		{ text: 'Wie fange ich an?', href: 'tutorial/start', icon: 'help-circle' },
		{ text: 'Vikus Viewer', href: 'tutorial/vikus_viewer', icon: 'search' },
		{ text: 'Künstliche Intelligenz', href: 'tutorial/ki', icon: 'cpu' },
		{ text: 'Machine Learning', href: 'tutorial/ml', icon: 'book-open' },
		{ text: 'Natural Language Processing', href: 'tutorial/nlp', icon: 'message-square' },
		{ text: 'Data Science', href: 'tutorial/ds', icon: 'database' }
	];
</script>

<Header />

<div class="flex flex-col text-center justify-center items-center mt-20">
	<h1
		class="mb-20 text-6xl font-bold uppercase text-gray-100 [text-shadow:0_4px_8px_rgba(255,255,255,0.25)]"
	>
		Willkommen zum Tutorial <br /> zur künstlichen Intelligenz
	</h1>

	<div class="flex flex-col gap-10">
		{#each redirects as redirect, i}
			<AnimationContainer delay={i <= 5 ? String(i * 0.5) + 's' : '0s'}>
				<TutorialRedirectButton text={redirect.text} href={redirect.href} icon={redirect.icon} />
			</AnimationContainer>
		{/each}
	</div>
</div>

<style lang="postcss">
</style>
