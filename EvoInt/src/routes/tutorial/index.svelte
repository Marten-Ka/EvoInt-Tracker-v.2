<script lang="ts">
	import Header from '../../components/Header.svelte';
	import AnimationContainer from '../../components/AnimationContainer.svelte';
	import TutorialRedirectButton from '../../components/_TutorialRedirectButton.svelte';
	import Footer from '../../components/Footer.svelte';

	const redirects = [
		{ text: 'Wie funktioniert der EvoInt-Tracker?', href: 'tutorial/start', icon: 'help-circle' },
		{ text: 'Künstliche Intelligenz', href: 'tutorial/ki', icon: 'cpu' },
		{ text: 'Machine Learning', href: 'tutorial/ml', icon: 'book-open' },
		{ text: 'Natural Language Processing', href: 'tutorial/nlp', icon: 'message-square' }
	];
</script>

<Header />

<div class="flex flex-col text-center justify-center items-center mt-20 mb-96">
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

<Footer />

<style lang="postcss">
</style>
