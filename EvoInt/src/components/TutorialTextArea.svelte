<script lang="ts">
	import Icon from './Icon.svelte';
	export let icon: string;
	export let icon_size: string;
	export let icon_color: string;
	export let content: string = '';
</script>

<div class="max-w-4xl xl:max-w-6xl 2xl:max-w-7xl mt-12 mb-80">
	<div class="block p-8 pr-12 rounded-lg shadow-lg bg-white m-4">
		<div class="md:flex md:flex-row">
			<div class="md:w-96 w-36 flex flex-col gap-4 mt-1 items-center mb-6 lg:mb-0 mx-auto md:mx-0">
				<Icon {icon} size={icon_size} color={icon_color} />
			</div>
			<div class="md:ml-6 place-self-center">
				{#if content}
					<p class="text-gray-700 text-justify text-base sm:text-lg md:text-xl lg:text-2xl">{content}</p>
				{:else}
					<slot name="content" />
				{/if}
			</div>
		</div>
	</div>
</div>

<style lang="postcss">
</style>
